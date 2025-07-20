
import logging
from bson import ObjectId
from dotenv import load_dotenv
import os
from scripts.what_if import analyze_student
# Setup
load_dotenv()
MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


student1 =ObjectId("66ad3ea0711e23168f7a937a")
student2 = ObjectId("65aafd6d9acfd21d1abbfaae")
analyze_student (student1)  
analyze_student(student2 )

