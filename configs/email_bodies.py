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
    <p>I am writing to express my interest in the <b>{interst}</b> {applying_for} position at {companyName}. </p>
    <p>In the past, I have worked as a <b>{prev_title}</b> at a Digital Business Transformation Company called {prev_company} for {exp_in_years} years. </p>
    <p>I think I would be a great fit for your organization because of the following reasons:</p>
    <ol>
      <li>I have a strong technical background with proficiency in <b>{technical_skills_1}</b>. </li>
      <li>I have a firm grasp of <b>AWS</b>. I am also a <b>GCP Certified</b>
        <a href="{userCertificationURL}">Associate Cloud Engineer</a>.
      </li>
      <li>I have a deep understanding of designing streaming and batch ETL jobs using <b>{technical_skills_3}</b> along with data libraries such as <b>Pandas, and Numpy</b>, Job Schedulers such as <b>Airflow</b> and <b>Jenkins</b></li>
      <li>I have expertise in designing and deploying infrastucture using <b>{technical_skills_4}.</b> </li>
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
      p {{
        margin-bottom: 10px;
        line-height: 1.5;
      }}
    </style>
  </head>
  <body>
    <p>Dear Professor,</p>
    <p>I hope this email finds you in good health and high spirits!</p>
    <p>My name is <b>{userFirstName} {userLastName}</b>, and I am a passionate Master's student in {currentMajor} with {currentGPA} GPA. I am writing to express my strong interest in the <b>Grader, TA, and Lab Assistant</b> positions for the upcoming semester.</p>
    <p>During the previous semesters at the esteemed Tempe campus, I had the privilege of taking the following courses, which enriched my knowledge and skills:</p>
    <ol>
    {subjectList}
    </ol>
    <p>Prior to my graduate studies, I pursued my undergraduate degree in {prevMajor} Engineering, achieving an outstanding CGPA of {prevGPA}. Throughout my academic journey, I consistently demonstrated dedication and excellence in my coursework.</p>
    <p>Moreover, I have gained valuable experience in grading assignments as a grader under Dr. Pramod Kumar at ASU last semester. This role allowed me to develop strong attention to detail and provide constructive feedback to students.</p>
    <p>I deeply value your time and consideration, and I am truly grateful for the opportunity to apply for the <b>Grader, TA, and Lab Assistant positions</b>. </p>
    <p>I eagerly await the chance to contribute my skills, knowledge, and passion and to create a positive and engaging learning environment for students. With my dedication and enthusiasm, I am confident in my ability to assist both students and faculty members effectively.</p>
<p>Thank you once again for your time and attention. I wish you an amazing day!</p>
<p>Sincerely,</p>
<p>{userFirstName} {userLastName}</p>

  </body>
</html>"""
