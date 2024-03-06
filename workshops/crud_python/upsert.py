import os
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

new_team = {
    "name": "Aston Villa",
    "league": "Premier League",
    "country": "England",
}

# Update or insert the new team
result = teams_collection.update_one(
    {"name": new_team["name"]},
    {"$set": new_team},
    upsert=True
)

document_id = result.upserted_id
print(f"Inserted new team with ID: {document_id}")

client.close()
