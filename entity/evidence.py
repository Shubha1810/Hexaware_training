class Evidence:
    def __init__(self, evidence_id=None, description="", location_found="", incident_id=None):
        self.__evidence_id = evidence_id
        self.__description = description
        self.__location_found = location_found
        self.__incident_id = incident_id

    def get_evidence_id(self): return self.__evidence_id
    def set_evidence_id(self, evidence_id): self.__evidence_id = evidence_id

    def get_description(self): return self.__description
    def set_description(self, description): self.__description = description

    def get_location_found(self): return self.__location_found
    def set_location_found(self, location_found): self.__location_found = location_found

    def get_incident_id(self): return self.__incident_id
    def set_incident_id(self, incident_id): self.__incident_id = incident_id

    def __str__(self):
        return f"Evidence[ID={self.__evidence_id}, Found At={self.__location_found}]"
