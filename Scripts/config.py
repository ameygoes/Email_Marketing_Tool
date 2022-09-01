# THIS DEFINES YOUR MAIN FOLDER AFTER THE ROOT FILE_FOLDER
# ROOT FOLDER IS WHERE YOUR SENDEMAILUSINGGMAIL SCRIPT IS LOCATED
FILE_FOLDER = "Data"

# THIS IS THE FILENAME OF CSV FILE WHICH CONTAINS DETAILS OF THE HRs
FILE_NAME = "inputData.csv"

# THIS IS THE FOLDER WHERE RESUME AND CV IS LOCATED
RESUME_FOLDER = "Resume"

# THIS IS YOUR FILE NAME OF RESUME AND COVERLETTER
RESUME_FILE_NAME="Amey_Bhilegaonkar.pdf"
COVER_LETTER_FILE_NAME = "Amey_Bhilegaonkar.pdf"

# SKILL SET DICTINARY DEFINES A CERTAIN VALUES DEPENDING ON THE JOB TITLE YOU WANT TO APPLY FOR
# THE KEY FOR THE DICTIONARY COMES FROM THE INPUT CSV FILE - COL - POSITION
# WE ALSO NEED TO MAKE SURE WE HAVE THE SIMILAR FOLDER STRUCTURE FOR DATA LIKE RESUME AND CV ALSO

# SKILLS
SKILL_SET = {
    "SDE" : {
        "SKILLS" : "Java, Spring boot, Python, Django, Databases, Cloud Technologies, Springboot, Apache Spark, Cassandra, Kafka, Airflow, Pandas, Keras",
        "TITLE" : "Associate Software Development Engineer 2",
        "LOOKING_TITLE": "Software Development Engineer / Backend Engineer",
        "NATURAL_INTERESTS": "computer science, Data Structure and Algorithms, Distributed Systems, Backend Engineering"
    },

    "DEVOPS" : {
        "SKILLS" : "AWS, GCP, Terraform, Jenkins, Docker, Kubernetes, CICD, Python, Java, Bash, Linux, Automation, Databases, DevOps, Git and Version control, code refactoring",
        "TITLE" : "Associate Devops Engineer",
        "LOOKING_TITLE": "DevOps Engineer / SRE",
        "NATURAL_INTERESTS": "computer science, Cloud Technologies, Automation"
    },
    "DATA" : {
        "SKILLS" : "Python,TensorFlow, Keras, PyTorch, MySQL, scikit-learn, Numpy, Scipy, Jupyter, Pandas, Apache Spark, Airflow, Distributed Databases Systems, Data Cleaning, Data Extraction, Data Visualization",
        "TITLE" : "Data Analyst and Data Engineer",
        "LOOKING_TITLE": "Data Scientist and Data Analyst",
        "NATURAL_INTERESTS": "Data Science, Machine Learning, Data Engineering"
    },
}

PRONOUNS = {
"M" : "Mr.",
"F" : "Ms."
}

# ADD YOUR PERSONAL DETAILS HERE TO SEND ALONG WITH MAIL
PERSONAL_DETAILS = """
Mobile    : +1-480-616-3980.
Email     : amey.bhilegaonkar@asu.edu
PortFolio : https://ameyportfolio.netlify.app
LinkedIn  : https://www.linkedin.com/in/amey-bhilegaonkar/
"""

# EMAIL BODY
INTERN_REFERAL = """ \
Dear {proNoun} {firstName} {lastName},

My name is Amey Bhilegaonkar, and I am a graduate student at the Arizona State University,
pursuing my Masters in Computer Science with specialization in Data Science this fall.

I am looking for a Summer Internship 2023 opportunities for the roles {aspiring_role_title} and {companyName} caught my eye as a place
where I could make a difference.

Because of my background and natural interest in {natural_interests},
I am writing to see if you could refer me for the positions for student Summer Internships in the {aspiring_role_title} sector.

In the past, I have worked at a Digital Business Transformation Company called Publicis Sapient for 3+ years
as the {roleTitle} which really helped me gain skills and professional experience on, {profesional_skills}.

I have taken classes in my bachelors which helped me strenthen my computer science concepts, and I am taking in my masters classes that will
help my sharpen the edges, building strong understanding and foundations to work as an SDE.

{companyName} is at the top of my list of internships and I am very interested in hearing more about it.

I have also attached my resume with this email and my details are as below:
{personalDetails}

Thanks,
"""

# THIS IS NOT CURRENTLY IN USE BUT IS FOR FUTURE USE
followUpBody = """
Dear {proNoun} {firstName} {lastName},

I hope this message findexs you well!
I recently inquired about a possible summer internship with {companyName} and wanted to be sure to follow up.
I am very interested in working with {companyName} and would love the opportunity to speak with you regarding the Summer Intern Position.
I appreciate your time and hope to have the chance to speak with you soon.

Best,

"""
