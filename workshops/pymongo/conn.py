
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from .env file
load_dotenv("config.env")
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

# List all databases in the cluster
for db_name in client.list_database_names():
    print(db_name)

client.close()
