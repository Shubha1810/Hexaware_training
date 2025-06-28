from abc import ABC, abstractmethod


class ICrimeAnalysisService(ABC):

    @abstractmethod
    def create_incident(self, incident): pass

    @abstractmethod
    def update_incident_status(self, incident_id, new_status): pass

    @abstractmethod
    def get_incidents_in_date_range(self, start_date, end_date): pass

    @abstractmethod
    def search_incidents(self, incident_type): pass

    @abstractmethod
    def generate_incident_report(self, incident_id): pass

    @abstractmethod
    def create_case(self, description, incident_ids): pass

    @abstractmethod
    def get_case_details(self, case_id): pass

    @abstractmethod
    def update_case_details(self, case_id, new_description): pass

    @abstractmethod
    def get_all_cases(self): pass
