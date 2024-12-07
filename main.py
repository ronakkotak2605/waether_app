import logging
from logger_config import setup_logger
from modules.api_handler import APIHandler
from modules.data_processor import DataProcessor

def main():
    setup_logger()
    logger = logging.getLogger(__name__)

    logger.info("Weather app started")
    api_handler = APIHandler()
    data_processor = DataProcessor()

    city = input("Enter city name: ")
    weather_data = api_handler.fetch_weather(city)
    if weather_data:
        processed_data = data_processor.process_weather_data(weather_data)
        print(processed_data)

if __name__ == "__main__":
    main()
