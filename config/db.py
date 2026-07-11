import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = None
db     = None

def init_db(app=None):
    global client, db
    uri = os.getenv("MONGO_URI")
    if not uri:
        raise RuntimeError(
            "MONGO_URI environment variable is not set. "
            "Set it in your Railway service variables (Settings > Variables)."
        )
    client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True, serverSelectionTimeoutMS=10000)
    db     = client.get_default_database()
    print(f"Connected to MongoDB: {db.name}")

def get_db():
    return db