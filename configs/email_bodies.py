# EMAIL BODY  {lastName}
INTERN_REFERAL = """
<!DOCTYPE html>
<html>
  <head>
    <style>
      p {{
          margin-bottom: 10px;
          line-height: 1.5;
      }}
    </style>
  </head>
  <body>
    <p>Hi {firstName},</p>
    <p>Hope you are doing well!</p>
    <p>I am {userFirstName} {userLastName}, a Computer Science graduate student at <b>Arizona State University</b>. </p>
    <p>I am writing to express my interest in the <b>Data Engineering and Analytics</b> {applying_for} position at {companyName}. </p>
    <p>In the past, I have worked as a <b>Data Engineer and DevOps Engineer</b> at a Digital Business Transformation Company called Publicis Sapient for 3+ years. </p>
    <p>I think I would be a great fit for your organization because of the following reasons:</p>
    <ol>
      <li>I have a strong technical background with proficiency in <b>SQL</b>, <b>Python</b>, <b>Scalable ETL Pipeline Designing</b>, <b>Java</b>, <b>Apache Spark</b>. </li>
      <li>I have a firm grasp of <b>AWS</b>. I am also a <b>GCP Certified</b>
        <a href="{userCertificationURL}">Associate Cloud Engineer</a>.
      </li>
      <li>I have a deep understanding of <b>CICD</b>, <b>DevOps and Automation tools</b>, <b>Docker</b>, and <b> Kafka </b>along with data libraries such as <b>Pandas, and Numpy</b>, Job Schedulers such as <b>Airflow</b> and <b>Jenkins</b>
      </li>
    </ol>
    <p>I have <b>{soft_skills}</b>. I am excited about the opportunity to join <b>{companyName}</b> and contribute to the company's mission. </p>
    <p>
      <b>{companyName}</b> is my top priority and I look forward to hearing from you.
    </p>
    <p>Thank you for taking the time to consider my request. Have an amazing rest of the day.</p>
    <p>PS: I have also attached my resume with this email for your reference. If you need further information, feel free to contact me.</p>
    <p>My PortFolio: <a href="{userPortFolioURL}">{userPortFolioURL}</a>
    </p>
    <p>My GitHub: <a href="{userGitHubURL}">See {userFirstName}'s GitHub</a>
    </p>
    <p> Best, <br> {userFirstName} {userLastName} </p>
  </body>
</html> """

# THIS IS NOT CURRENTLY IN USE BUT IS FOR FUTURE USE
THANK_YOU_EMAIL = """
<!DOCTYPE html>
<html>
  <head>
    <style>
      p {
          {
          margin-bottom: 10px;
          line-height: 1.5;
        }
      }
    </style>
  </head>
  <body>
    <p>Dear {firstName},</p>
    <p>I would like to extend my sincere gratitude for taking the time to interview me for the position at {companyName}. It was a pleasure speaking with you about the company and the role. </p>
    <p>Thank you for your thoughtful questions and for providing me with additional information about the company's culture and goals.</p>
    <p>I appreciate your professionalism and the opportunity to discuss my qualifications for the position. Your insights into the company's values and the job requirements were very helpful, and I feel even more excited about the possibility of joining the team.</p>
    <p>Thank you again for considering me for this role, and I am truly looking forward to continuing our conversation. Please do not hesitate to contact me if you have any further questions or if there is anything else I can provide.</p>
    <p>Best regards,</p>
    <p> {userFirstName} {userLastName} </p>
  </body>
</html>
"""


SLIDING_INTO_DMS = """
<!DOCTYPE html>
<html>
  <head>
    <style>
      p {
        margin-bottom: 10px;
        line-height: 1.5;
      }
    </style>
  </head>
  <body>
    <p>Hello {firstName},</p>
    <p>Good morning!</p>
    <p>I hope this email finds you well. It was wonderful connecting with you last time. I recently applied to a few positions within {companyName}.</p>
    <p>I am reaching out to you because while I understand that you may not be the hiring manager or directly connected to the positions, I was wondering if there is a way for my credentials to be seen by someone who is connected to the relevant role.</p>
    <p>If confidentiality is a concern and you are not at liberty to provide me with the contact information of the person connected to the role, would it be possible for you to share my LinkedIn profile with some of your colleagues?</p>
    <p>I greatly appreciate your time, and I understand if you are busy. I have been consistently applying to {companyName} positions and I am hoping to get noticed soon.</p>
    <p>Thank you for considering my request. Wishing you an amazing day ahead.</p>
    <p>My Details: <a href="{userPortFolioURL}">{userPortFolioURL}</a></p>
    <p>Best wishes,</p>
    <p>{userFirstName} {userLastName}</p>
  </body>
</html>
"""


GRADER_MAIL = """
<!DOCTYPE html>
<html>
  <head>
    <style>
      p {
        margin-bottom: 10px;
        line-height: 1.5;
      }
    </style>
  </head>
  <body>
    <p>Hi Professor,</p>
    <p>Hope this email finds you well!</p>
    <p>I am <b>Amey Bhilegaonkar</b>, a Master's student in Computer Science, writing to apply for the <b>Grader, Tutor, TA, and Lab Assistant</b> job opportunity for <b>Spring 2023</b>. </p>
    <p>In the <b>fall 2022</b> semester at the Tempe campus, I took the following courses: </p>
    <ol>
      <li>CSE 575 Statistical Machine Learning</li>
      <li>CSE 594 Spatial Data Science</li>
      <li>CSE 543 Information Assurance and Security</li>
    </ol>
    <p>In <b>Spring 2023</b>, I am enrolled in the following courses: </p>
    <ol>
      <li>Data Processing at Scale</li>
      <li>Data Mining</li>
      <li>Knowledge Representation</li>
    </ol>
    <p>I have completed my undergraduate studies in Electronics and Telecommunications Engineering with a CGPA of 8.78/10. Additionally, I have experience grading assignments for a private tuition teacher and have provided tutoring and mentoring to several juniors.</p>
    <p>I also conduct online helping sessions called " <b>A helping hand</b>" for undergraduate students on LinkedIn. </p>
    <p>During my undergraduate studies, I led the Machine Learning Club, where I mentored juniors and promoted awareness of projects and research in the field of Machine Learning and Data Science. I worked on projects such as Emotion Detection using Speech and Images and developed an End-to-End project to streamline the college's training and placement process.</p>
    <p>Furthermore, I have over <b>3 years of experience</b> as a <b>Data Engineer</b> at Publicis Sapient, a Digital Business Transformation company. My role involved working on Distributed Database Systems, Cloud technologies (AWS, GCP), Design Patterns, SDLC, Agile, and DevOps. </p>
    <p>I understand that your time is valuable, and I appreciate your consideration for the <b>Grader, Tutor, TA, and Lab Assistant positions</b>. I hope to hear from you soon. </p>
    <p>Thank you for your time. Wishing you an amazing day!</p>
    <p>PS: I have attached my resume and transcripts to this email. You can also find my portfolio at <a href="https://ameyportfolio.netlify.app">https://ameyportfolio.netlify.app</a>. </p>
    <p>Thank you,</p>
    <p>Amey Bhilegaonkar</p>
  </body>
</html>"""
