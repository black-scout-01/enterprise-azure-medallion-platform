from dotenv import load_dotenv
import os

load_dotenv()

AZURE_STORAGE_ACCOUNT = os.getenv("AZURE_STORAGE_ACCOUNT")
AZURE_STORAGE_KEY = os.getenv("AZURE_STORAGE_KEY")

BRONZE_CONTAINER = os.getenv("BRONZE_CONTAINER")
SILVER_CONTAINER = os.getenv("SILVER_CONTAINER")
GOLD_CONTAINER = os.getenv("GOLD_CONTAINER")