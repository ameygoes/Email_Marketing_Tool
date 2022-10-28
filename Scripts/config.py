# THIS DEFINES YOUR MAIN FOLDER AFTER THE ROOT FILE_FOLDER
# ROOT FOLDER IS WHERE YOUR SENDEMAILUSINGGMAIL SCRIPT IS LOCATED
FILE_FOLDER = "Data"

# THIS IS THE FILENAME OF CSV FILE WHICH CONTAINS DETAILS OF THE HRs
FILE_NAME = "Google.csv"
# FILE_NAME = "inputData.csv"

# ASKING_FOR = "referral" #"folloupUniv"
ASKING_FOR = "folloupUniv"

# THIS IS THE FOLDER WHERE RESUME AND CV IS LOCATED
RESUME_FOLDER = "Resume"

# THIS IS YOUR FILE NAME OF RESUME AND COVERLETTER
RESUME_FILE_NAME="AmeyBhilegaonkarMastersResume.pdf"
COVER_LETTER_FILE_NAME = "Amey_Bhilegaonkar.pdf"


OUTPUT_FOLDER = "output"
OUTPUT_FILE = "mailingOutput.txt"


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
        "SKILLS" : "Python, MySQL, Pandas, Apache Spark, Airflow, Distributed Databases Systems, Data Cleaning, Data Extraction, Data Visualization",
        "TITLE" : "Data Analyst and Data Engineer",
        "LOOKING_TITLE": "Data Engineer and Data Science",
        "NATURAL_INTERESTS": "Data Engineering, Distributed Systems, and Large Data Processing"
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

# EMAIL BODY  {lastName}
INTERN_REFERAL = """Hi {firstName},<br>
<br>
Hope you are doing well!
<br>
<br>
Hi, I am Amey Bhilegaonkar, a Computer Science graduate student at Arizona State University.<br>
<br>
I am looking for Summer Internship 2023(May-August) opportunities for the {aspiring_role_title} roles, and {companyName}
caught my eye as a place where I could make a difference.<br>
<br>

In the past, I have worked at a Digital Business Transformation Company called Publicis Sapient for 3+ years
as the {roleTitle} which helped me gain skills and professional experience in, {profesional_skills}.<br>
<br>
I am reaching out to you because while I understand you may not be the hiring manager or connected to the position,
Confidentiality is understood so if you are not at liberty to give me the information to the person connected to the role,
is there some way that you can share my LinkedIn profile/ Resume with some of your colleagues?<br>
Or could you please give me a referral for the open position?
<br>
<br>
{companyName} is my top priority and I looking forward to hearning from you.<br>
<br>

Your time is valuable and I understand if you don’t have the bandwidth. I’ve been consistently applying to the {companyName} and I’m hoping to be noticed soon. <br>
Thank you for taking the time to consider my request. Have an amazing rest of the day.
<br>
<br>
PS: I have also attached my resume with this email for your reference. If you need further information, feel free to contact me. <br>
My Details: https://ameyportfolio.netlify.app

<br>
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
<br>

Best,

"""


followUpBody2 = """
Hello {firstName}, <br>
<br>
Good morning! <br>
<br>
I hope all is well. My name is Amey and it is wonderful to connect with you. I applied to a few positions within {companyName}. <br>
<br>
I am reaching out to you because while I understand you may not be the hiring manager or connected to the position, <br>
<br>
I was wondering if there was a way my credentials can be seen by someone connected to the position. <br>
<br>
Confidentiality is understood so if you are not at liberty to give me the information to the person connected to the role, <br>
is there some way that you can share my LinkedIn profile with some of your colleagues?
<br>
Your time is valuable and I understand if you don’t have the bandwidth. I’ve been consistently applying to the {companyName} and I’m hoping to be noticed soon. <br>
<br>
Thank you for taking the time to consider my request. Have an amazing rest of the day. <br>
<br>

My Details: https://ameyportfolio.netlify.app

<br>
<br>
Best wishes, <br>
<br>
Amey Bhilegaonkar

"""


graderMail = """

"""
