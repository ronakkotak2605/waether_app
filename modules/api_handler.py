import requests
import logging
from config_reader import ConfigReader

logger = logging.getLogger(__name__)

class APIHandler:
    def __init__(self):
        self.config = ConfigReader()
        self.base_url = self.config.get("API", "base_url")
        self.api_key = self.config.get("API", "api_key")

    def fetch_weather(self, city):
        logger.info(f"Fetching weather data for city: {city}")
        params = {"q": city, "appid": self.api_key}
        try:
            response = requests.get(self.base_url, params=params)

            response.raise_for_status()
            logger.info("API call successful")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error during API call: {e}")
            return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    api_handler = APIHandler()
    print(api_handler.fetch_weather("London"))
