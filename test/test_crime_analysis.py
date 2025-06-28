import unittest
from dao.crime_analysis_service_impl import CrimeAnalysisServiceImpl
from entity.incident import Incident
from datetime import date


class TestCrimeAnalysis(unittest.TestCase):
    def setUp(self):
        self.service = CrimeAnalysisServiceImpl()

    def test_create_incident(self):
        incident = Incident(
            incident_type="test type",
            incident_date=date.today().isoformat(),
            latitude=10.0,
            longitude=20.0,
            description="test incident",
            status="open",
            victim_id=1,
            suspect_id=1,
            agency_id=1
        )
        result = self.service.create_incident(incident)
        self.assertTrue(result)

    def test_update_incident_status(self):
        # Update incident ID 1 to status 'closed'
        updated = self.service.update_incident_status(1, "closed")
        self.assertTrue(updated)

    def test_update_invalid_incident_status(self):
        with self.assertRaises(Exception):
            self.service.update_incident_status(9999, "closed")  # assuming 9999 doesn't exist


if __name__ == '__main__':
    unittest.main()
