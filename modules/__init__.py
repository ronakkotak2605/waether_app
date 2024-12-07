"""
This __init__.py file makes the modules directory a Python package.
It dynamically imports and exposes all key classes or functions from the modules
to simplify imports for the end user.
"""
import logging
# Configure logging for the modules package
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


from .api_handler import APIHandler
from .data_processor import DataProcessor

__all__ = ["APIHandler", "DataProcessor"]

if __name__ == "__main__":
    print("Modules package is successfully loaded!")
