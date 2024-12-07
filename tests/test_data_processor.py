import unittest
from modules.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def test_process_weather_data_invalid(self):
        data = None
        result = DataProcessor.process_weather_data(data)
        self.assertIsNone(result)

    def test_process_weather_data_valid(self):
        data = {
            "name": "London",
            "main": {"temp": 280},
            "weather": [{"description": "cloudy"}]
        }
        result = DataProcessor.process_weather_data(data)
        self.assertEqual(result["city"], "London")

if __name__ == "__main__":
    unittest.main()
