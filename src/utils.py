import os
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_binance_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API_KEY and API_SECRET must be set in the .env file.")

    # Connect to Binance Futures Testnet using built-in flag
    client = Client(api_key, api_secret, testnet=True)
    return client
