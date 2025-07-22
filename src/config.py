import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration class to hold all the application settings from environment variables.
    """
    # eBay API Credentials
    EBAY_APP_ID = os.getenv('EBAY_APP_ID')
    EBAY_CERT_ID = os.getenv('EBAY_CERT_ID')
    EBAY_DEV_ID = os.getenv('EBAY_DEV_ID')
    EBAY_RU_NAME = os.getenv('EBAY_RU_NAME')

    # MongoDB Connection
    MONGO_URI = os.getenv('MONGO_URI')

    # Search Parameters
    SEARCH_KEYWORDS = os.getenv('SEARCH_KEYWORDS', 'laptop,phone').split(',')

config = Config()
