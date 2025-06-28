class Report:
    def __init__(self, report_id=None, incident_id=None, reporting_officer=None, report_date="", report_details="", status=""):
        self.__report_id = report_id
        self.__incident_id = incident_id
        self.__reporting_officer = reporting_officer
        self.__report_date = report_date
        self.__report_details = report_details
        self.__status = status

    def get_report_id(self): return self.__report_id
    def set_report_id(self, report_id): self.__report_id = report_id

    def get_incident_id(self): return self.__incident_id
    def set_incident_id(self, incident_id): self.__incident_id = incident_id

    def get_reporting_officer(self): return self.__reporting_officer
    def set_reporting_officer(self, reporting_officer): self.__reporting_officer = reporting_officer

    def get_report_date(self): return self.__report_date
    def set_report_date(self, report_date): self.__report_date = report_date

    def get_report_details(self): return self.__report_details
    def set_report_details(self, report_details): self.__report_details = report_details

    def get_status(self): return self.__status
    def set_status(self, status): self.__status = status

    def __str__(self):
        return f"Report[ID={self.__report_id}, Officer={self.__reporting_officer}, Status={self.__status}]"
