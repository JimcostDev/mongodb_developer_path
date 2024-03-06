import os
import pprint
from dotenv import load_dotenv
from pymongo import MongoClient
# from bson.objectid import ObjectId

# Load config from .env file
load_dotenv("config.env")
MONGODB_URI = os.getenv("MONGODB_URI")

# Connect to the MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to the football database
db = client.football

# Get reference to the teams collection
teams_collection = db.teams

# Query by league
documents_to_find = {
    "league": "Premier League"
}

# write an expression to insert multiple documents
cursor = teams_collection.find(documents_to_find, {"name": 1, "_id": 0}).sort("name", 1)

num_documents = 0
for document in cursor:
    num_documents += 1
    pprint.pprint(document)
print(f"Number of documents found: {num_documents}")

client.close()
