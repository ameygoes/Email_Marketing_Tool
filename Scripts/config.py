# THIS DEFINES YOUR MAIN FOLDER AFTER THE ROOT FILE_FOLDER
# ROOT FOLDER IS WHERE YOUR SENDEMAILUSINGGMAIL SCRIPT IS LOCATED
FILE_FOLDER = "Data"

# THIS IS THE FILENAME OF CSV FILE WHICH CONTAINS DETAILS OF THE HRs
# FILE_NAME = "teacherEmails.csv"
FILE_NAME = "Teacher.csv"

# ASKING_FOR = "referral" #"folloupUniv"
# ASKING_FOR = "folloupUniv"
ASKING_FOR = "grader"

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
Dear Professor, <br>
<br>
I am <strong> Amey Bhilegaonkar</strong>, a Master's in Computer Science student for the Fall 2022 term with ASU ID: 1225368924, <br>
writing to apply for <strong>Grader, Tutor, and Lab Assistant</strong> job opportunity for <strong> Spring 2023 </strong>.
<br>
Currently, I am enrolled in the below courses at the Tempe campus:<br>

1. CSE 575 Statistical Machine Learning
<br>
2. CSE 594 Spatial Data Science
<br>
3. CSE 543 Information Assurance and Security
<br>

I have completed my undergraduate studies in Electronics and Telecommunications Engineering with a CGPA of 8.78 out of 10. I have some experience in grading assignments in two subjects during my undergrad. <br>
Also, I've assisted and mentored several juniors as a tutor and helped them clear their doubts and get good grades. <br>
<br>
I’ve taken the following coursework from various domains in my undergraduate studies:
<br>
    1. Data Structures and Algorithms <br>
    2. Object Oriented Programming with C++ and Java<br>
    3. Systems Programming and Operating System<br>
    4. Data Base Management System<br>
    5. Computer Networks<br>
    6. Artificial Intelligence<br>
    7. Engineering Mathematics 1,2,3<br>
    8. Machine Learning<br>
    9. Microprocessors and Microcontrollers<br>
    10. Digital Image Processing<br>
<br>

During my undergraduate study, I lead Machine Learning Club along with my teammate, which was focused on guiding and mentoring juniors and making them aware of projects and research going on in the field of Machine Learning and Data science.<br>
I also worked on projects like Emotion Detection using Speech and Images. Build my End-to-End software which was used to ease out the training and placement process for the college. <br>


I also have 3+ years of experience working as a <strong>Data Analyst and Data Engineer</strong>, at a Digital Business transformation company called Publicis Sapient. <br>
At Publicis Sapient, I evolved as a Software Developer and learned many things, including Distributed Database Systems, Cloud technologies like AWS, GCP, Design Patterns, SDLC, Agile, DevOps, etc.<br>
<br>
Your time is valuable and I understand if you don’t have the bandwidth. I’ve been consistently applying to the <strong>Grader, Tutor, and Lab Assistant positions </strong> and I’m hoping to be noticed soon. <br>
<br>
Thank you for taking the time to consider my request. Have an amazing rest of the day. <br>

PS: I have attached my resume with this mail, and here is my Portfolio: https://ameyportfolio.netlify.app
<br>
<br>
Thank You, <br>
<br>
Amey Bhilegaonkar
"""
