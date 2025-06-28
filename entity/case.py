class Case:
    def __init__(self, case_id=None, description="", incident_ids=None):
        self.__case_id = case_id
        self.__description = description
        self.__incident_ids = incident_ids or []  # List of incident IDs

    def get_case_id(self): return self.__case_id
    def set_case_id(self, case_id): self.__case_id = case_id

    def get_description(self): return self.__description
    def set_description(self, description): self.__description = description

    def get_incident_ids(self): return self.__incident_ids
    def set_incident_ids(self, incident_ids): self.__incident_ids = incident_ids

    def __str__(self):
        return f"Case[ID={self.__case_id}, Incidents={self.__incident_ids}]"
