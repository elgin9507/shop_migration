import os
from io import RawIOBase

from dotenv import load_dotenv

load_dotenv()

try:
    SHOPIFY_SHOP_URL = os.environ["SHOPIFY_SHOP_URL"]
    SHOPIFY_API_VERSION = os.environ["SHOPIFY_API_VERSION"]
    SHOPIFY_TOKEN = os.environ["SHOPIFY_TOKEN"]
    PRESTASHOP_WEBSERVICE_URL = os.environ["PRESTASHOP_WEBSERVICE_URL"]
    PRESTASHOP_WEBSERVICE_KEY = os.environ["PRESTASHOP_WEBSERVICE_KEY"]
except KeyError:
    raise RuntimeError(
        "Environment not configured properly. Please refer to the documentation to setup environment variables."
    )
