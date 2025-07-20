from pymongo import MongoClient
from bson.objectid import ObjectId
from .scorer import get_score
import logging
from dotenv import load_dotenv
import os


load_dotenv()


MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
attempts_collection = db["results"]

def analyze_student(student_id):
    
    attempts = list(attempts_collection.find({"student_id": student_id}))
    # print("Attemts ==========",attempts)
    if not attempts:
        logging.warning(f"No attempts found for user: {student_id}")
        return

    # Group attempts by subject and level
    grouped = {}
    for att in attempts:
        subject_obj = att.get("subject", {})
        subject_name = subject_obj.get("name")
        level = att.get("compleixty")  
        correct = att.get("correct", 0)

        if not subject_name or not level:
            # logging.warning(f"Skipping malformed attempt: {att}")
            continue

        grouped.setdefault(subject_name, {}).setdefault(level, []).append(correct)

    total_scores = {}

    for subject in grouped:
        levels = grouped[subject]
        total_raw = sum([sum(levels[level]) for level in levels])

        module2_level = "easy" if "easy" in levels and "hard" not in levels else "hard"

        score_obj = get_score(subject, total_raw, module2_level)
        # if score_obj:
        #     scaled_score = score_obj.get(module2_level)
        #     logging.info(f"{subject} raw={total_raw}, level={module2_level}, scaled={scaled_score}")
        #     total_scores[subject] = scaled_score
        # else:
        #     logging.error(f"No scaled score found for {subject} with raw {total_raw}")
        # logging.info(f"{subject} raw={total_raw}, level={module2_level}, scaled={score_obj}")
        total_scores[subject] = score_obj
 
    math_score = total_scores.get("Math", 0)
    rw_score = total_scores.get("Reading and Writing", 0)  
    total = math_score + rw_score
    logging.info(f"Total Score for {student_id}: {total} (Math={math_score}, R&W={rw_score})")
