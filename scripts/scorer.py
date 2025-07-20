
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import os

import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
scoring_collection = db["scorings"]

def get_score(subject_key, raw_score, level, program="DSAT"):
    """
    Fetch scaled score from the scorings collection using cleaned subject key and difficulty.
    """
    # logging.info(f"Normalized subject_key: {scoring_collection}")
        # print( "====================",scoring_collection , "====================")
    subject_key = subject_key.strip().lower()  # Normalize input
    # print(scoring_collection , "====================") 
    # logging.info(f"Normalized subject_key: {subject_key}")
    doc = scoring_collection.find_one({
        "$expr": {
            "$and": [
                { "$eq": [ { "$toLower": "$key" }, subject_key ] },
                { "$eq": [ "$program", program ] }
            ]

        }
    })

    if not doc:
        # print(f"[WARN] No scoring document found for '{subject_key}' in program '{program}'")
        return 0

    for entry in doc.get("map", []):
        if entry.get("raw") == raw_score:
            score = entry.get(level.lower(), 0)
            if score == 0:
                print(f"[WARN] No score for level '{level}' at raw={raw_score} for subject '{subject_key}'")
            return score

    print(f"[WARN] No matching raw score {raw_score} found for subject '{subject_key}'")
    return 0
