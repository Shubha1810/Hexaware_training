from dao.crime_analysis_service_impl import CrimeAnalysisServiceImpl
from entity.incident import Incident
from exception.incident_not_found_exception import IncidentNumberNotFoundException


def validate_field(field_value, field_name):
    if not field_value.strip():
        raise ValueError(f"{field_name} should not be empty.")
    return field_value.strip()


def main():
    service = CrimeAnalysisServiceImpl()

    while True:
        print("\n--- Crime Analysis and Reporting System ---")
        print("1. Create Incident")
        print("2. Update Incident Status")
        print("3. Get Incidents in Date Range")
        print("4. Search Incidents by Type")
        print("5. Generate Incident Report")
        print("6. Create New Case")
        print("7. Get Case Details")
        print("8. Update Case Details")
        print("9. Get All Cases")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == '1':
                # --- Create Incident ---
                print("\n--- Create New Incident ---")
                i_type = validate_field(input("Incident Type: "), "Incident Type")
                i_date = validate_field(input("Incident Date (YYYY-MM-DD): "), "Incident Date")
                lat = validate_field(input("Latitude: "), "Latitude")
                lon = validate_field(input("Longitude: "), "Longitude")
                desc = validate_field(input("Description: "), "Description")
                status = validate_field(input("Status (Open/Closed/etc): "), "Status")
                vic_id = validate_field(input("Victim ID: "), "Victim ID")
                sus_id = validate_field(input("Suspect ID: "), "Suspect ID")
                ag_id = validate_field(input("Agency ID: "), "Agency ID")

                # Create and insert Incident
                incident = Incident(
                    incident_type=i_type,
                    incident_date=i_date,
                    latitude=float(lat),
                    longitude=float(lon),
                    description=desc,
                    status=status,
                    victim_id=int(vic_id),
                    suspect_id=int(sus_id),
                    agency_id=int(ag_id)
                )
                incident_id = service.create_incident(incident)
                if incident_id:
                    print(f" Incident created successfully with Incident ID: {incident_id}")
                else:
                    print(" Failed to create incident.")

            elif choice == '2':
                # --- Update Incident Status ---
                print("\n--- Update Incident Status ---")
                incident_id = int(validate_field(input("Enter Incident ID: "), "Incident ID"))
                new_status = validate_field(input("Enter New Status: "), "Status")

                success = service.update_incident_status(incident_id, new_status)
                print(" Status updated successfully!" if success else " Failed to update status.")

            elif choice == '3':
                # --- Get Incidents in Date Range ---
                print("\n--- Search Incidents by Date Range ---")
                start = validate_field(input("Enter Start Date (YYYY-MM-DD): "), "Start Date")
                end = validate_field(input("Enter End Date (YYYY-MM-DD): "), "End Date")

                results = service.get_incidents_in_date_range(start, end)
                if results:
                    for row in results:
                        print(row)
                else:
                    print(" No incidents found in the specified date range.")

            elif choice == '4':
                # --- Search Incidents by Type ---
                print("\n--- Search Incidents by Type ---")
                i_type = validate_field(input("Enter Incident Type: "), "Incident Type")
                results = service.search_incidents(i_type)
                if results:
                    for row in results:
                        print(row)
                else:
                    print(" No incidents found of this type.")

            elif choice == '5':
                # --- Generate Incident Report ---
                print("\n--- Generate Incident Report ---")
                incident_id = int(validate_field(input("Enter Incident ID: "), "Incident ID"))
                report = service.generate_incident_report(incident_id)
                print(report)

            elif choice == '6':
                # --- Create New Case ---
                print("\n--- Create New Case ---")
                description = validate_field(input("Enter Case Description: "), "Case Description")
                ids = validate_field(input("Enter Incident IDs (comma-separated): "), "Incident IDs")

                id_list = [int(x.strip()) for x in ids.split(',') if x.strip().isdigit()]
                if not id_list:
                    print(" Invalid incident IDs.")
                    continue

                case_id = service.create_case(description, id_list)
                if case_id:
                    print(f" Case created successfully with Case ID: {case_id}")
                else:
                    print(" Failed to create case.")

            elif choice == '7':
                # --- Get Case Details ---
                print("\n--- View Case Details ---")
                case_id = int(validate_field(input("Enter Case ID: "), "Case ID"))
                details = service.get_case_details(case_id)
                print(details)

            elif choice == '8':
                # --- Update Case Details ---
                print("\n--- Update Case Description ---")
                case_id = int(validate_field(input("Enter Case ID: "), "Case ID"))
                new_desc = validate_field(input("Enter New Description: "), "New Description")

                updated = service.update_case_details(case_id, new_desc)
                print("Case updated successfully." if updated else " Update failed.")

            elif choice == '9':
                # --- Get All Cases ---
                print("\n--- List of All Cases ---")
                cases = service.get_all_cases()
                if cases:
                    for case in cases:
                        print(case)
                else:
                    print(" No cases found.")

            elif choice == '10':
                print("Exiting the system. Goodbye!")
                break

            else:
                print(" Invalid choice. Please try again.")

        except ValueError as ve:
            print(f" Input Error: {ve}")
        except IncidentNumberNotFoundException as ine:
            print(f" {ine}")
        except Exception as e:
            print(f" Unexpected error: {e}")


if __name__ == '__main__':
    main()
