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
documente_to_delete = {"name": "Werder Bremen"}

# Search for document before delete
print("Searching for target document before delete: ")
pprint.pprint(teams_collection.find_one(documente_to_delete))

# Delete
result = teams_collection.delete_one(documente_to_delete)

# Search for document after delete
print("Searching for target document after delete: ")
pprint.pprint(teams_collection.find_one(documente_to_delete))

client.close()
