
import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "escola_db")

# Conexão simples e síncrona
_client = MongoClient(MONGO_URI)
_db = _client[MONGO_DB]

def get_db():
    return _db
