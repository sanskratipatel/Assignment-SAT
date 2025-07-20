import json
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

collection = db["user_attempts"]
with open("C:\\Users\\Sanskrati\\Desktop\\NEWFOLDER\\Assignment-SAT\\data\\67f2aae2c084263d16dbe462user_attempt_v2.json", "r") as f:

# with open("C:\\Users\\Sanskrati\\Desktop\\NEWFOLDER\\Assignment-SAT\\data\\66fece285a916f0bb5aea9c5user_attempt_v3.json", "r") as f:
    data = json.load(f)

for doc in data:
    id_fields = ["_id", "student_id", "question_id", "practicesetId", "parentTest"]
    for k in id_fields:
        if k in doc and isinstance(doc[k], str):
            try:
                doc[k] = ObjectId(doc[k])
            except:
                pass
    for fld in ("subject", "unit", "topic"):
        if fld in doc and "_id" in doc[fld] and isinstance(doc[fld]["_id"], str):
            doc[fld]["_id"] = ObjectId(doc[fld]["_id"])

for doc in data[:5]: 
    try:
        collection.insert_one(doc)
        print(f"Inserted: {doc['_id']}")
    except Exception as e:
        print(f" Error inserting {doc.get('_id', 'unknown')}: {e}")

print(f" Inserted {len(data)} documents (dropped & reinserted).")
