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

# Query by name
document_to_find = {
    "name": "Liverpool"
}


# write an expression to insert multiple documents
result = teams_collection.find_one(document_to_find)
pprint.pprint(result)

client.close()
