import unittest
from modules.api_handler import APIHandler

class TestAPIHandler(unittest.TestCase):
    def setUp(self):
        self.api_handler = APIHandler()

    def test_fetch_weather_invalid_city(self):
        response = self.api_handler.fetch_weather("InvalidCity")
        self.assertIsNone(response)

if __name__ == "__main__":
    unittest.main()
