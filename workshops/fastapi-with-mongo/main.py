from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

# Obtener la variable de entorno MONGODB_URI
MONGODB_URI = os.getenv("MONGODB_URI")

# Conectar al clúster de MongoDB con MongoClient
client = MongoClient(MONGODB_URI)

# Obtener la referencia a la base de datos football
db = client.football

# Obtener la referencia a la colección de equipos
teams_collection = db.teams

@app.get("/", tags=["Teams"])
async def get_teams():
    # Consulta por liga
    filter = {}

    # Escribir una expresión para insertar varios documentos
    cursor = teams_collection.find(filter, {"_id": 0}).sort("name", 1)

    teams = []
    for document in cursor:
        teams.append(document)

    return {"teams": teams}