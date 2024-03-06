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

new_teams = {
    "name": "Werder Bremen",
    "league": "Bundesliga",
    "country": "Germany"
},  {
    "name": "RB Leipzig",
    "league": "Bundesliga",
    "country": "Germany"

}

# write an expression to insert multiple documents
result = teams_collection.insert_many(new_teams)

documents_ids = result.inserted_ids
print(f"# of documents inserted: {len(documents_ids)}")
print(f"_ids of inserted documents: {documents_ids}")

client.close()
