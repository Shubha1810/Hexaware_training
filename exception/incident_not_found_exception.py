class IncidentNumberNotFoundException(Exception):
    def __init__(self, message="incident id not found in database"):
        super().__init__(message)
