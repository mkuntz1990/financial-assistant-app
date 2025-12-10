# Example test for backend API endpoints using mock data
import unittest
from backend.tests import test_data

class TestBackendAPI(unittest.TestCase):
    def test_version_response(self):
        response = test_data.get_mock_response("version")
        self.assertIn("version", response)
        self.assertEqual(response["version"], "1.2.3")

    def test_update_response(self):
        response = test_data.get_mock_response("update")
        self.assertTrue(response["update_available"])
        self.assertEqual(response["latest_version"], "1.2.3")

    def test_health_response(self):
        response = test_data.get_mock_response("health")
        self.assertEqual(response["status"], "ok")

    def test_ping_response(self):
        response = test_data.get_mock_response("ping")
        self.assertTrue(response["pong"])

if __name__ == "__main__":
    unittest.main()
