class Incident:
    def __init__(self, incident_id=None, incident_type="", incident_date="", latitude=0.0, longitude=0.0,
                 description="", status="", victim_id=None, suspect_id=None, agency_id=None):
        self.__incident_id = incident_id
        self.__incident_type = incident_type
        self.__incident_date = incident_date
        self.__latitude = latitude
        self.__longitude = longitude
        self.__description = description
        self.__status = status
        self.__victim_id = victim_id
        self.__suspect_id = suspect_id
        self.__agency_id = agency_id

    # Getters and setters
    def get_incident_id(self): return self.__incident_id
    def set_incident_id(self, incident_id): self.__incident_id = incident_id

    def get_incident_type(self): return self.__incident_type
    def set_incident_type(self, incident_type): self.__incident_type = incident_type

    def get_incident_date(self): return self.__incident_date
    def set_incident_date(self, incident_date): self.__incident_date = incident_date

    def get_latitude(self): return self.__latitude
    def set_latitude(self, latitude): self.__latitude = latitude

    def get_longitude(self): return self.__longitude
    def set_longitude(self, longitude): self.__longitude = longitude

    def get_description(self): return self.__description
    def set_description(self, description): self.__description = description

    def get_status(self): return self.__status
    def set_status(self, status): self.__status = status

    def get_victim_id(self): return self.__victim_id
    def set_victim_id(self, victim_id): self.__victim_id = victim_id

    def get_suspect_id(self): return self.__suspect_id
    def set_suspect_id(self, suspect_id): self.__suspect_id = suspect_id

    def get_agency_id(self): return self.__agency_id
    def set_agency_id(self, agency_id): self.__agency_id = agency_id

    def __str__(self):
        return f"Incident[ID={self.__incident_id}, Type={self.__incident_type}, Date={self.__incident_date}]"
