import os
import pprint
from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from .env file
load_dotenv("config.env")
MONGODB_URI = os.getenv("MONGODB_URI")

# Connect to the MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to the football database
db = client.football

# Get reference to the teams collection
teams_collection = db.teams

# Filter
documente_to_update = {"name": "Aston Villa"}

# Update
change_name = {"$set": {"name": "Arsenal"}}

# Update the document
result = teams_collection.update_one(
    documente_to_update,
    change_name
)
print(f"Updated {result.modified_count} document")

client.close()
