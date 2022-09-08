# THIS DEFINES YOUR MAIN FOLDER AFTER THE ROOT FILE_FOLDER
# ROOT FOLDER IS WHERE YOUR SENDEMAILUSINGGMAIL SCRIPT IS LOCATED
FILE_FOLDER = "Data"

# THIS IS THE FILENAME OF CSV FILE WHICH CONTAINS DETAILS OF THE HRs
FILE_NAME = "apollo-contacts-export.csv"

# THIS IS THE FOLDER WHERE RESUME AND CV IS LOCATED
RESUME_FOLDER = "Resume"

# THIS IS YOUR FILE NAME OF RESUME AND COVERLETTER
RESUME_FILE_NAME="AmeyBhilegaonkarMastersResume.pdf"
COVER_LETTER_FILE_NAME = "Amey_Bhilegaonkar.pdf"

# SKILL SET DICTINARY DEFINES A CERTAIN VALUES DEPENDING ON THE JOB TITLE YOU WANT TO APPLY FOR
# THE KEY FOR THE DICTIONARY COMES FROM THE INPUT CSV FILE - COL - POSITION
# WE ALSO NEED TO MAKE SURE WE HAVE THE SIMILAR FOLDER STRUCTURE FOR DATA LIKE RESUME AND CV ALSO

# SKILLS
SKILL_SET = {
    "SDE" : {
        "SKILLS" : "Java, Spring boot, Python, Django, Databases, Cloud Technologies, Springboot, Apache Spark, Cassandra, Kafka, Airflow, Pandas, Keras",
        "TITLE" : "Associate Software Development Engineer 2",
        "LOOKING_TITLE": "Software Development Engineer",
        "NATURAL_INTERESTS": "computer science, Data Structure and Algorithms, Distributed Systems, and Backend Engineering"
    },

    "DEVOPS" : {
        "SKILLS" : "AWS, GCP, Terraform, Jenkins, Docker, Kubernetes, CICD, Python, Java, Bash, Linux, Automation, Databases, DevOps, Git and Version control, code refactoring",
        "TITLE" : "Associate DevOps Engineer",
        "LOOKING_TITLE": "DevOps Engineer / SRE",
        "NATURAL_INTERESTS": "computer science, Cloud Technologies, and Automation"
    },
    "DATA" : {
        "SKILLS" : "Python, TensorFlow, Keras, PyTorch, MySQL, scikit-learn, Numpy, Scipy, Jupyter, Pandas, Apache Spark, Airflow, Distributed Databases Systems, Data Cleaning, Data Extraction, Data Visualization",
        "TITLE" : "Data Analyst and Data Engineer",
        "LOOKING_TITLE": "Data Science, Data Analysis, or Data Engineer",
        "NATURAL_INTERESTS": "Data Science, Machine Learning, and Data Engineering"
    },
}

PRONOUNS = {
"M" : "Mr.",
"F" : "Ms."
}

# ADD YOUR PERSONAL DETAILS HERE TO SEND ALONG WITH MAIL
PERSONAL_DETAILS = """
PortFolio : https://ameyportfolio.netlify.app
"""

# EMAIL BODY
INTERN_REFERAL = """Hi {firstName} {lastName},<br>
<br>
Hope you are doing well!
<br>
<br>
Hi, I am Amey Bhilegaonkar, a graduate student at Arizona State University,
pursuing my master's in Computer Science with a specialization in Data Science this fall.<br>
<br>
I am looking for Summer Internship 2023(May-August) opportunities for the {aspiring_role_title} roles, and {companyName}
caught my eye as a place where I could make a difference.<br>
<br>
In the past, I have worked at a Digital Business Transformation Company called Publicis Sapient for 3+ years
as the {roleTitle} which helped me gain skills and professional experience in, {profesional_skills}.<br>
<br>
Because of my background and natural interest in {natural_interests},
I wanted to check with you if you have any {aspiring_role_title} Co-op/Internship opportunities for Summer 2023 (May - August).<br>
<br>
{companyName} is my top priority and I am very interested in hearing more about it.<br>
<br>
I have also attached my resume with this email for your reference. If you need further information, feel free to contact me. <br>

<br>

I look forward to hearing from you.<br>
<br>
Thanks and regards,
<br>
Amey
<br >

"""

# THIS IS NOT CURRENTLY IN USE BUT IS FOR FUTURE USE
followUpBody = """
Dear {firstName} {lastName},

I hope this message findexs you well!
I recently inquired about a possible summer internship with {companyName} and wanted to be sure to follow up.
I am very interested in working with {companyName} and would love the opportunity to speak with you regarding the Summer Intern Position.
I appreciate your time and hope to have the chance to speak with you soon.

Best,

"""
