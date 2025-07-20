

# import logging
# from pymongo import MongoClient
# from bson import ObjectId
# from dotenv import load_dotenv
# import os

# # Setup
# load_dotenv()
# from dotenv import load_dotenv


# MONGO_URI = os.getenv("MONGODB_URI")
# DB_NAME = os.getenv("DB_NAME")


# # Logging config
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger()

# # Connect to DB
# client = MongoClient(MONGO_URI)
# db = client[DB_NAME]
# attempts_col = db["results"]


# SCORE_SCALE = {
#     "easy": 210,
#     "medium": 300,
#     "hard": 390
# }

# def calculate_scores(student_id: str):
#     student_obj_id = ObjectId(student_id)
#     attempts = list(attempts_col.find({"student_id": student_obj_id}))

#     logger.info(f"\n--- Analyzing student: {student_id} ---")
#     logger.info(f"Total Attempts Found: {len(attempts)}")

#     total_score = 0
#     math_score = 0
#     rw_score = 0

#     for attempt in attempts:
#         subject = attempt.get("subject", {}).get("name", "").strip()
#         complexity = attempt.get("compleixty", "").lower()
#         correct = attempt.get("correct", 0)

#         # Log subject and complexity
#         logger.info(f"Attempt: subject='{subject}', correct={correct}, level='{complexity}'")

#         if correct == 1 and complexity in SCORE_SCALE:
#             scaled_score = SCORE_SCALE[complexity]
#             if subject.lower() == "math":
#                 math_score += scaled_score
#                 logger.info(f"Math raw={correct}, level={complexity}, scaled={scaled_score}")
#             elif subject.lower() == "reading and writing":
#                 rw_score += scaled_score
#                 logger.info(f"Reading and Writing raw={correct}, level={complexity}, scaled={scaled_score}")
#             else:
#                 logger.warning(f"Unknown subject '{subject}' — skipping.")

#     total_score = math_score + rw_score
#     logger.info(f"Total Score for {student_id}: {total_score} (Math={math_score}, R&W={rw_score})\n")


import logging
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os
from scripts.what_if import analyze_student
# Setup
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

# Logging config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# === Run analysis for students === 
student1 =ObjectId("66ad3ea0711e23168f7a937a")
student2 = ObjectId("65aafd6d9acfd21d1abbfaae")
analyze_student (student1)  # Replace with actual ObjectId strings
analyze_student(student2 )

