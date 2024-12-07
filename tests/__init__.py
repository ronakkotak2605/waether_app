"""
This __init__.py file makes the tests directory a Python package.
It can include initialization logic for tests or utilities.
"""

# Import key test modules for easier access if needed
from .test_api_handler import TestAPIHandler
from .test_data_processor import TestDataProcessor

__all__ = ["TestAPIHandler", "TestDataProcessor"]

if __name__ == "__main__":
    print("Tests package is successfully loaded!")
