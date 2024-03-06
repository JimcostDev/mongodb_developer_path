
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import pprint

# Load config from .env file
load_dotenv("config.env")
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

# Get reference to the football database
db = client.football

# Get reference to 'scorers' collection
scorers_collection = db.scorers

# Select players with more than 19 goals
select_players = {'$match': {'goles': {'$gt': 19}}}

# Group by league and calculate the total number of goals and players
scorers_by_league = {'$group': {'_id': '$torneo',
                                'total': {'$sum': 1},
                                'goles': {'$sum': '$goles'},
                                'jugadores': {'$addToSet': '$jugador'}}
                     }
# Sort by the number of goals
organize_by_league = {'$sort': {'goles': -1}}

# Execute the aggregation pipeline
pipilene = [select_players,
            scorers_by_league,
            organize_by_league]

results = scorers_collection.aggregate(pipilene)

print()
print("Players with more than 19 goals by league:")

for doc in results:
    pprint.pprint(doc)

client.close()
