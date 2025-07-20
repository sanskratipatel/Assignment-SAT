import json
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()



MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db["scorings"]

# Load data from scoring.json
with open("C:\\Users\\Sanskrati\\Desktop\\NEWFOLDER\\Assignment-SAT\\data\\scoring_DSAT_v2.json") as file:
    data = json.load(file)

# Drop existing data
collection.drop()

# Insert each document individually
for doc in data:
    # Ensure _id is an actual ObjectId
    if "_id" in doc and isinstance(doc["_id"], dict) and "$oid" in doc["_id"]:
        doc["_id"] = ObjectId(doc["_id"]["$oid"])
    else:
        doc["_id"] = ObjectId()

    # Ensure subjectId is an ObjectId
    if "subjectId" in doc and isinstance(doc["subjectId"], dict) and "$oid" in doc["subjectId"]:
        doc["subjectId"] = ObjectId(doc["subjectId"]["$oid"])

    collection.insert_one(doc)

print(f" Inserted {len(data)} scoring documents into 'scorings' collection with ObjectId types.")
