import logging

logger = logging.getLogger(__name__)

class DataProcessor:
    @staticmethod
    def process_weather_data(data):
        if not data or "main" not in data:
            logger.error("Invalid weather data")
            return None

        logger.info("Processing weather data")
        weather_info = {
            "city": data.get("name"),
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        logger.debug(f"Processed data: {weather_info}")
        return weather_info

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sample_data = {
        "name": "London",
        "main": {"temp": 280},
        "weather": [{"description": "cloudy"}]
    }
    print(DataProcessor.process_weather_data(sample_data))
