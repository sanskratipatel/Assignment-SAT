
# SAT Adaptive Score Analysis

This project analyzes SAT student performance using adaptive scoring logic based on their responses and question difficulty. It uses MongoDB for dynamic data fetching and provides insight into student performance and what-if analysis (e.g., What if the student had answered this question correctly? ).


## 🗂 Project Structure

```
___data /     
│
├── scripts/
│   ├── score.py                  
│   ├── resultdatainsert.py       # Inserts student attempts into MongoDB `results` collection
│   └── scoredatainsert.py        # Inserts scoring mappings into MongoDB `scorings` collection        
│   └── what_if.py 
├── main.py                         
├── requirements.txt              
├── .env                            # Environment variables for MongoDB URI and DB name
└── README.md                       
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone 
cd Assignment-SAT
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate


### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

---
##  Populate MongoDB Data

Make sure MongoDB is running locally or remotely.

1. Create a `.env` file in the root directory with:

```env
MONGODB_URI= URL
DB_NAME=SAT  (other db name)
```

2. Insert sample datasets:

```bash
# Inserts student test results into the `results` collection
python resultdatasetinsert.py

# Inserts SAT adaptive scoring logic into the `scorings` collection
python scoredatasetinsert.py
```

---


To run the analysis:

```bash
python main.py
```

This will print the analysis log for each student, including:

* Total attempts per subject
* Correct answers and their difficulty
* Scaled score
* What-if suggestions (e.g., impact of incorrect answers if they had been correct)

---

##  Example Output

```
--- Analyzing student: 66ad3ea0711e23168f7a937a ---
Total Attempts Found: 2
Attempt: subject='Math', correct=2, level='medium'
Scaled Score for attempt: 630
What if the student had answered all questions correctly?
+80 points possible increase in Math
```

---

## Dependencies



```
dnspython==2.7.0
numpy==2.3.1
pandas==2.3.1
pymongo==4.13.2
python-dateutil==2.9.0.post0
python-dotenv==1.1.1
pytz==2025.2
six==1.17.0
tzdata==2025.2
```

Install them using:

```bash
pip install -r requirements.txt
```
Thanks For Reading This..................
