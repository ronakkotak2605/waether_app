weather_app/
├── config.cfg           # Configuration file for storing API keys, endpoints
├── config_reader.py     # Reads config.cfg
├── logger_config.py     # Centralized logger configuration
├── main.py              # Entry point of the application
├── modules/
│   ├── __init__.py      # Marks modules as a package
│   ├── api_handler.py   # Handles API interactions
│   ├── data_processor.py # Processes API response data
├── tests/
│   ├── __init__.py      # Marks tests as a package
│   ├── test_api_handler.py # Unit tests for api_handler.py
│   ├── test_data_processor.py # Unit tests for data_processor.py
