from dao.crime_analysis_service_impl import CrimeAnalysisServiceImpl
from entity.incident import Incident
from exception.incident_not_found_exception import IncidentNumberNotFoundException
from util.geocode_util import GeoCodeUtil
from datetime import date, datetime
from decimal import Decimal
from tabulate import tabulate



def validate_field(field_value, field_name):
    if not field_value.strip():
        raise ValueError(f"{field_name} should not be empty.")
    return field_value.strip()


def validate_date_input(date_str, field_name):
    date_str = validate_field(date_str, field_name)
    try:
        valid_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        return valid_date.isoformat()
    except ValueError:
        raise ValueError(f"❌ Invalid {field_name}. Please enter a valid date in YYYY-MM-DD format.")


def format_row(row):
    return tuple(
        str(item) if isinstance(item, (Decimal, datetime, date)) else item for item in row
    )

def print_table(data, headers):
    if not data:
        print("No data found.")
    else:
        formatted_data = [format_row(row) for row in data]
        print(tabulate(formatted_data, headers=headers, tablefmt="fancy_grid"))

def main():
    service = CrimeAnalysisServiceImpl()

    while True:
        print("\n==== Crime Analysis and Reporting System (C.A.R.S.) ====")

        print("\n--- Add / Record Data ---")
        print("1. Add new incident")
        print("2. Change status of incident")
        print("3. Add victim details")
        print("4. Add suspect details")
        print("5. Add officer details")
        print("6. Add agency details")
        print("7. Add evidence")
        print("8. Create a report for an incident")

        print("\n--- View / Search Data ---")
        print("9. View all incidents")
        print("10. View all victims")
        print("11. View all suspects")
        print("12. View all officers")
        print("13. View all agencies")
        print("14. List incidents in a date range")
        print("15. Search incidents by type")

        print("\n--- Case Management ---")
        print("16. Add a case with incidents")
        print("17. View case details")
        print("18. Edit case description")
        print("19. View all cases")

        print("\n--- Reporting ---")
        print("20. Incident Reports")
        print("21. Case Reports")

        print("\n22. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == '1':
                print("\n--- Create New Incident ---")
                i_type = validate_field(input("Incident Type: "), "Incident Type")

                i_date_input = input("Incident Date (YYYY-MM-DD): ").strip()
                if not i_date_input:
                    i_date = date.today().isoformat()
                    print(f"✔ No date entered. Using today's date: {i_date}")
                else:
                    i_date = validate_date_input(i_date_input, "Incident Date")

                location_name = validate_field(input("Enter Location (City/Area): "), "Location")
                lat, lon = GeoCodeUtil.get_coordinates(location_name)
                if lat is None or lon is None:
                    print("❌ Could not fetch coordinates. Please try a valid location.")
                    continue
                print(f" Location found: Latitude = {lat}, Longitude = {lon}")

                desc = validate_field(input("Description: "), "Description")
                status = validate_field(input("Status (Open/Closed/etc): "), "Status")

                victim_id = service.get_latest_id("victims", "victimid")
                suspect_id = service.get_latest_id("suspects", "suspectid")
                agency_id = service.get_latest_id("law_enforcement_agencies", "agencyid")

                if victim_id is None or suspect_id is None or agency_id is None:
                    print(
                        "Could not fetch required IDs. Please ensure victims, suspects, and law_enforcement_agencies tables have data.")
                    continue

                incident = Incident(
                    incident_type=i_type,
                    incident_date=i_date,
                    latitude=lat,
                    longitude=lon,
                    description=desc,
                    status=status,
                    victim_id=victim_id,
                    suspect_id=suspect_id,
                    agency_id=agency_id
                )

                incident_id = service.create_incident(incident)
                if incident_id:
                    print(f"Incident created successfully with Incident ID: {incident_id}")
                else:
                    print("❌ Failed to create incident.")

            elif choice == '2':
                print("\n--- Update Incident Status ---")
                incident_id = int(validate_field(input("Enter Incident ID: "), "Incident ID"))
                new_status = validate_field(input("Enter New Status: "), "Status")
                success = service.update_incident_status(incident_id, new_status)
                print("Status updated successfully!" if success else "Failed to update status.")

            elif choice == '3':
                print("\n--- Add Victim ---")
                fname = validate_field(input("First Name: "), "First Name")
                lname = validate_field(input("Last Name: "), "Last Name")
                dob = validate_date_input(input("Date of Birth (YYYY-MM-DD): "), "Date of Birth")
                gender = validate_field(input("Gender: "), "Gender")
                contact = validate_field(input("Contact Info (Email ID): "), "Contact Info")

                if "@gmail.com" not in contact.lower():
                    print("❌ Contact Info must be a valid Gmail ID (e.g., name@gmail.com).")
                    continue

                success = service.add_victim(fname, lname, dob, gender, contact)
                print(" Victim added successfully." if success else "❌ Failed to add victim.")

            elif choice == '4':
                print("\n--- Add Suspect ---")
                fname = validate_field(input("First Name: "), "First Name")
                lname = validate_field(input("Last Name: "), "Last Name")
                dob = validate_date_input(input("Date of Birth (YYYY-MM-DD): "), "Date of Birth")
                gender = validate_field(input("Gender: "), "Gender")
                contact = validate_field(input("Contact Info (Email ID): "), "Contact Info")

                if "@gmail.com" not in contact.lower():
                    print("❌ Contact Info must be a valid Gmail ID (e.g., name@gmail.com).")
                    continue

                success = service.add_suspect(fname, lname, dob, gender, contact)
                print("Suspect added successfully." if success else "❌ Failed to add suspect.")

            elif choice == '5':
                print("\n--- Add Officer ---")
                fname = validate_field(input("First Name: "), "First Name")
                lname = validate_field(input("Last Name: "), "Last Name")
                badge = validate_field(input("Badge Number (e.g., B1001): "), "Badge Number")
                rank = validate_field(input("Rank (e.g., Inspector, Sub-Inspector, Constable): "), "Rank")
                contact = validate_field(input("Contact Info (Email ID): "), "Contact Info")
                if "@gmail.com" not in contact.lower():
                    print("❌ Contact Info must be a valid Gmail ID (e.g., name@gmail.com).")
                    return
                agency_id = service.get_latest_id("law_enforcement_agencies", "agencyid")
                success = service.add_officer(fname, lname, badge, rank, contact, agency_id)
                print("Officer added successfully." if success else "Failed to add officer.")

            elif choice == '6':
                print("\n--- Add Agency ---")
                name = validate_field(input("Agency Name (e.g., Central Police Station): "), "Agency Name")
                jurisdiction = validate_field(input("Jurisdiction (e.g., Zone A): "), "Jurisdiction")
                contact = validate_field(input("Contact Info (Email ID, e.g., central@police.gov): "), "Contact Info")
                if not contact.endswith("@police.gov"):
                    print("❌ Invalid email format. Must end with @police.gov")
                    return
                success = service.add_agency(name, jurisdiction, contact)
                print("✅ Agency added successfully." if success else "❌ Failed to add agency.")

            elif choice == '7':
                print("\n--- Add Evidence ---")
                desc = validate_field(input("Description: "), "Description")
                location = validate_field(input("Location Found: "), "Location Found")
                inc_id = int(validate_field(input("Incident ID: "), "Incident ID"))
                success = service.add_evidence(desc, location, inc_id)
                print("Evidence added successfully." if success else "Failed to add evidence.")

            elif choice == '8':
                print("\n--- Generate Incident Report ---")
                incident_id = int(validate_field(input("Enter Incident ID: "), "Incident ID"))
                report = service.generate_incident_report(incident_id)
                print(report)

            elif choice == '9':
                results = service.get_all_incidents()
                headers = ["ID", "Type", "Date", "Latitude", "Longitude", "Description", "Status", "Victim ID",
                           "Suspect ID", "Agency ID"]
                print_table(results, headers) if results else print("No incidents found.")

            elif choice == '10':
                results = service.get_all_victims()
                headers = ["ID", "First Name", "Last Name", "DOB", "Gender", "Contact"]
                print_table(results, headers)

            elif choice == '11':
                results = service.get_all_suspects()
                headers = ["ID", "First Name", "Last Name", "DOB", "Gender", "Contact"]
                print_table(results, headers)

            elif choice == '12':
                results = service.get_all_officers()
                headers = ["ID", "First Name", "Last Name", "Badge", "Rank", "Contact", "Agency ID"]
                print_table(results, headers)

            elif choice == '13':
                results = service.get_all_agencies()
                headers = ["ID", "Name", "Jurisdiction", "Contact"]
                print_table(results, headers)


            elif choice == '14':
                print("\n--- Search Incidents ---")
                print("1. Search by Date Range")
                print("2. Search by Year")
                print("3. Search by Month and Year")
                sub_choice = input("Enter your choice: ").strip()

                if sub_choice == '1':
                    start = validate_date_input(input("Enter Start Date (YYYY-MM-DD): "), "Start Date")
                    end = validate_date_input(input("Enter End Date (YYYY-MM-DD): "), "End Date")
                    results = service.get_incidents_in_date_range(start, end)

                elif sub_choice == '2':
                    year = validate_field(input("Enter Year (e.g., 2024): "), "Year")
                    query = "SELECT * FROM incidents WHERE YEAR(incidentdate) = %s"
                    results = service.run_custom_query(query, (year,))

                elif sub_choice == '3':
                    year = validate_field(input("Enter Year (e.g., 2024): "), "Year")
                    month = validate_field(input("Enter Month (1-12): "), "Month")
                    query = "SELECT * FROM incidents WHERE YEAR(incidentdate) = %s AND MONTH(incidentdate) = %s"
                    results = service.run_custom_query(query, (year, month))

                else:
                    print(" Invalid sub-choice.")
                    continue

                if results:
                    for row in results:
                        print(format_row(row))
                else:
                    print(" No incidents found for the selected filter.")

            elif choice == '15':
                i_type = validate_field(input("Enter Incident Type: "), "Incident Type")
                results = service.search_incidents(i_type)
                headers = ["ID", "Type", "Date", "Latitude", "Longitude", "Description", "Status", "Victim ID",
                           "Suspect ID", "Agency ID"]
                print_table(results, headers)

            elif choice == '16':
                print("\n--- Create New Case ---")
                description = validate_field(input("Enter Case Description: "), "Case Description")
                ids = validate_field(input("Enter Incident IDs (comma-separated): "), "Incident IDs")
                id_list = [int(x.strip()) for x in ids.split(',') if x.strip().isdigit()]
                if not id_list:
                    print("Invalid incident IDs.")
                    return
                case_id = service.create_case(description, id_list)
                print(f"Case created successfully with Case ID: {case_id}" if case_id else "Failed to create case.")

            elif choice == '17':
                case_id = int(validate_field(input("Enter Case ID: "), "Case ID"))
                details = service.get_case_details(case_id)
                print(details)

            elif choice == '18':
                case_id = int(validate_field(input("Enter Case ID: "), "Case ID"))
                new_desc = validate_field(input("Enter New Description: "), "New Description")
                updated = service.update_case_details(case_id, new_desc)
                print("Case updated successfully." if updated else "Update failed.")

            elif choice == '19':
                cases = service.get_all_cases()
                headers = ["ID", "Description", "Created At"]
                print_table(cases, headers)

            elif choice == '20':
                print("\n--- Incident Reports ---")
                print("1. Incidents Created Today")
                print("2. Incidents Created This Month")
                print("3. Incidents Created This Year")
                print("4. Incidents in a Date Range")
                print("5. Incidents in Specific Month and Year")
                sub_choice = input("Enter your choice: ").strip()

                today = date.today()
                if sub_choice == '1':
                    results = service.get_incidents_in_date_range(today.isoformat(), today.isoformat())
                elif sub_choice == '2':
                    query = "SELECT * FROM incidents WHERE MONTH(incidentdate) = %s AND YEAR(incidentdate) = %s"
                    results = service.run_custom_query(query, (today.month, today.year))
                elif sub_choice == '3':
                    query = "SELECT * FROM incidents WHERE YEAR(incidentdate) = %s"
                    results = service.run_custom_query(query, (today.year,))
                elif sub_choice == '4':
                    start = validate_date_input(input("Enter Start Date (YYYY-MM-DD): "), "Start Date")
                    end = validate_date_input(input("Enter End Date (YYYY-MM-DD): "), "End Date")
                    results = service.get_incidents_in_date_range(start, end)
                elif sub_choice == '5':
                    year = validate_field(input("Enter Year (e.g., 2025): "), "Year")
                    month = validate_field(input("Enter Month (1-12): "), "Month")
                    query = "SELECT * FROM incidents WHERE YEAR(incidentdate) = %s AND MONTH(incidentdate) = %s"
                    results = service.run_custom_query(query, (year, month))
                else:
                    print(" Invalid sub-choice.")
                    continue
                if results:
                    for row in results:
                        print(format_row(row))
                else:
                    print(" No incidents found for the selected report.")

            elif choice == '21':
                print("\n--- Case Reports ---")
                print("1. Cases Created Today")
                print("2. Cases Created This Month")
                print("3. Cases Created This Year")
                print("4. Cases in a Date Range")
                print("5. Cases in Specific Month and Year")
                sub_choice = input("Enter your choice: ").strip()

                today = date.today()
                if sub_choice == '1':
                    query = "SELECT * FROM cases WHERE DATE(created_at) = %s"
                    results = service.run_custom_query(query, (today.isoformat(),))
                elif sub_choice == '2':
                    query = "SELECT * FROM cases WHERE MONTH(created_at) = %s AND YEAR(created_at) = %s"
                    results = service.run_custom_query(query, (today.month, today.year))
                elif sub_choice == '3':
                    query = "SELECT * FROM cases WHERE YEAR(created_at) = %s"
                    results = service.run_custom_query(query, (today.year,))
                elif sub_choice == '4':
                    start = validate_date_input(input("Enter Start Date (YYYY-MM-DD): "), "Start Date")
                    end = validate_date_input(input("Enter End Date (YYYY-MM-DD): "), "End Date")
                    query = "SELECT * FROM cases WHERE DATE(created_at) BETWEEN %s AND %s"
                    results = service.run_custom_query(query, (start, end))
                elif sub_choice == '5':
                    year = validate_field(input("Enter Year (e.g., 2025): "), "Year")
                    month = validate_field(input("Enter Month (1-12): "), "Month")
                    query = "SELECT * FROM cases WHERE YEAR(created_at) = %s AND MONTH(created_at) = %s"
                    results = service.run_custom_query(query, (year, month))
                else:
                    print(" Invalid sub-choice.")
                    return
                headers = ["ID", "Description", "Created At"]
                print_table(results, headers) if results else print(" No cases found for the selected report.")

            elif choice == '22':
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except IncidentNumberNotFoundException as ine:
            print(f"{ine}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == '__main__':
    main()
