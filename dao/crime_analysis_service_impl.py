import mysql.connector
from util.db_conn_util import DBConnUtil
from exception.incident_not_found_exception import IncidentNumberNotFoundException


class CrimeAnalysisServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def create_incident(self, incident):
        try:
            cursor = self.conn.cursor()
            query = """INSERT INTO incidents 
                       (incidenttype, incidentdate, location_latitude, location_longitude, 
                        description, status, victimid, suspectid, agencyid)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (incident.get_incident_type(), incident.get_incident_date(), incident.get_latitude(),
                      incident.get_longitude(), incident.get_description(), incident.get_status(),
                      incident.get_victim_id(), incident.get_suspect_id(), incident.get_agency_id())
            cursor.execute(query, values)
            self.conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error creating incident: {e}")
            return None

    def update_incident_status(self, incident_id, new_status):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM incidents WHERE incidentid = %s", (incident_id,))
            if cursor.fetchone() is None:
                raise IncidentNumberNotFoundException(f"Incident ID {incident_id} not found.")

            cursor.execute("UPDATE incidents SET status = %s WHERE incidentid = %s", (new_status, incident_id))
            self.conn.commit()
            return True
        except IncidentNumberNotFoundException as e:
            print(f"Custom Exception: {e}")
            return False
        except Exception as e:
            print(f"Error updating status: {e}")
            return False

    def get_incidents_in_date_range(self, start_date, end_date):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM incidents WHERE incidentdate BETWEEN %s AND %s"
            cursor.execute(query, (start_date, end_date))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching incidents in date range: {e}")
            return []

    def search_incidents(self, incident_type):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM incidents WHERE incidenttype = %s"
            cursor.execute(query, (incident_type,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error searching incidents: {e}")
            return []

    def generate_incident_report(self, incident_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM incidents WHERE incidentid = %s", (incident_id,))
            incident = cursor.fetchone()
            if not incident:
                raise IncidentNumberNotFoundException(f"Incident ID {incident_id} not found.")

            report = f"""
--- Incident Report ---
ID: {incident[0]}
Type: {incident[1]}
Date: {incident[2]}
Latitude: {incident[3]}
Longitude: {incident[4]}
Description: {incident[5]}
Status: {incident[6]}
Victim ID: {incident[7]}
Suspect ID: {incident[8]}
Agency ID: {incident[9]}
"""
            return report
        except IncidentNumberNotFoundException as e:
            return f"Custom Exception: {e}"
        except Exception as e:
            return f"Error generating report: {e}"

    def create_case(self, description, incident_ids):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO cases (description) VALUES (%s)", (description,))
            self.conn.commit()
            case_id = cursor.lastrowid

            for inc_id in incident_ids:
                cursor.execute("INSERT INTO case_incidents (caseid, incidentid) VALUES (%s, %s)", (case_id, inc_id))
            self.conn.commit()
            return case_id  # <-- return generated case ID
        except Exception as e:
            print(f"Error creating case: {e}")
            return None

    def get_case_details(self, case_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM cases WHERE caseid = %s", (case_id,))
            case = cursor.fetchone()
            if not case:
                return "Case not found."

            cursor.execute("SELECT incidentid FROM case_incidents WHERE caseid = %s", (case_id,))
            incidents = cursor.fetchall()
            return f"Case #{case[0]}: {case[1]} | Incidents: {[i[0] for i in incidents]}"
        except Exception as e:
            return f"Error retrieving case details: {e}"

    def update_case_details(self, case_id, new_description):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE cases SET description = %s WHERE caseid = %s", (new_description, case_id))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating case: {e}")
            return False

    def get_all_cases(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM cases")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving cases: {e}")
            return []
