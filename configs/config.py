import os
# THIS DEFINES YOUR MAIN FOLDER AFTER THE ROOT FILE_FOLDER
# ROOT FOLDER IS WHERE YOUR SENDEMAILUSINGGMAIL SCRIPT IS LOCATED
FILE_FOLDER = "Data"

# THIS IS THE FILENAME OF CSV FILE WHICH CONTAINS DETAILS OF THE HRs
# FILE_NAME = "inputData.csv"
FILE_NAME = "Teacher.csv"

# ASKING_FOR = "referral" #"folloupUniv"
# ASKING_FOR = "folloupUniv"
ASKING_FOR = "grader"


ENVIRONMENT = "DEV"  # - POSSIBLE VALUES - DEV, PROD

# THIS IS THE FOLDER WHERE RESUME AND CV IS LOCATED
# RESUME_FOLDER = os.path.join("C:", os.sep, "Amey", "Resume", "JP_Based_Resumes")
RESUME_FOLDER = os.path.join("D:", os.sep, "MY-DOCUMENTS", "RESUME", "JD", "DE")

# TRANSCRIPTS_FOLDER = os.path.join("C:", os.sep, "Amey", "MyDocuments")
TRANSCRIPTS_FOLDER = os.path.join("D:", os.sep, "study-code-repeat", "coding", "ASU_MCS", "FALL_22_CLASSES_SEM_1", "Grades")

# THIS IS YOUR FILE NAME OF RESUME AND COVERLETTER
RESUME_FILE_NAME = "AmeyBhilegaonkarResume.pdf"
COVER_LETTER_FILE_NAME = "Amey_Bhilegaonkar.pdf"
MS_TRANSCRIPTS_NAME = "Amey_Bhilegaonkar_Masters_Grades"
BE_TRANSCRIPTS_NAME = "AmeyBhilegaonkarTranscripts.pdf"


OUTPUT_FOLDER = "output"
OUTPUT_FILE = "mailingOutput.txt"


# SKILL SET DICTINARY DEFINES A CERTAIN VALUES DEPENDING ON THE JOB TITLE YOU WANT TO APPLY FOR
# THE KEY FOR THE DICTIONARY COMES FROM THE INPUT CSV FILE - COL - POSITION
# WE ALSO NEED TO MAKE SURE WE HAVE THE SIMILAR FOLDER STRUCTURE FOR DATA LIKE RESUME AND CV ALSO

# SKILLS
SKILL_SET = {
    "SDE": {
        "SKILLS": "Java, Spring boot, Python, Django, Databases, Cloud Technologies, Springboot, Apache Spark, Cassandra, Kafka, Airflow, Pandas, Keras",
        "TITLE": "Associate Software Development Engineer 2",
        "LOOKING_TITLE": "Software Development Engineer",
        "NATURAL_INTERESTS": "computer science, Data Structure and Algorithms, Distributed Systems, and Backend Engineering"
    },

    "DEVOPS": {
        "SKILLS": "AWS, GCP, Terraform, Jenkins, Docker, Kubernetes, CICD, Python, Java, Bash, Linux, Automation, Databases, DevOps, Git and Version control, code refactoring",
        "TITLE": "Associate DevOps Engineer",
        "LOOKING_TITLE": "DevOps Engineer / SRE",
        "NATURAL_INTERESTS": "computer science, Cloud Technologies, and Automation"
    },
    "DATA": {
        "SKILLS": "Python, MySQL, Pandas, Apache Spark, Airflow, Distributed Databases Systems, Data Cleaning, Data Extraction, Data Visualization",
        "TITLE": "Data Analyst and Data Engineer",
        "LOOKING_TITLE": "Data Engineer and Data Science",
        "NATURAL_INTERESTS": "Data Engineering, Distributed Systems, and Large Data Processing"
    },
}

PRONOUNS = {
    "M": "Mr.",
    "F": "Ms."
}

# ADD YOUR PERSONAL DETAILS HERE TO SEND ALONG WITH MAIL
PERSONAL_DETAILS = """
PortFolio : https://ameyportfolio.netlify.app
"""
