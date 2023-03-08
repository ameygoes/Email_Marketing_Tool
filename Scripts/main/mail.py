import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
import csv, pathlib
from configs.config import *
from configs.email_config import *
from configs.dbConfig import *
from utils.dbUtils import selectQuery
from datetime import date
from configs.envrinomentSpecificConfgis import TABLE_NAME, ASKING_FOR

class Mail:

    # INIT CONNECTION PARAMETERS 
    def __init__(self):
        self.port = SMTP_PORT
        self.smtp_server_domain_name = SMTP_DOMAIN_NAME
        self.sender_mail = FROM
        self.password = EMAIL_PASS

    # CHECK IF EMAIL PRESENT IN DB?
    def checkIfRecordPresentInDB(self,email_to_search):
        return selectQuery(SEARCH_QUERY.format(TABLE_NAME, "Email", email_to_search))

    # ATTACH FILE TO MAIL 
    def attachDocument(self, mail, file_Path, fname):
        mimeBase = MIMEBase("application", "octet-stream")
        with open(file_Path, "rb") as file:
            mimeBase.set_payload(file.read())
        encoders.encode_base64(mimeBase)
        mimeBase.add_header("Content-Disposition", f"attachment; filename={fname}")
        mail.attach(mimeBase)

    # UPDATE DATABASE / INSERT A ROW IN DATABASE
    def writeToOutputFile(self,first_Name, email, output, askingfor):
        today = date.today()
        with open(output, mode='a') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            if askingfor == "referral":
                employee_writer.writerow([first_Name, " ", email, f'Sent for referral on {today}'])
            elif askingfor == "folloupUniv":
                employee_writer.writerow([first_Name, " ", email, f'Sent for folloupUniv on {today}'])
            elif askingfor == "grader":
                employee_writer.writerow([first_Name, " ", email, f'Sent for grader on {today}'])

        print(f"Email Sent to: {email}")

    def getInternalReferalContent(self, first_Name, company, Position):
        return MIMEText(INTERN_REFERAL.format(
        firstName = first_Name,
        aspiring_role_title = SKILL_SET[Position]["LOOKING_TITLE"],
        companyName = company,
        roleTitle = SKILL_SET[Position]["TITLE"],
        # natural_interests = SKILL_SET[Position]["NATURAL_INTERESTS"],
        profesional_skills = SKILL_SET[Position]["SKILLS"],
        # personalDetails=PERSONAL_DETAILS
        ), 'html')

    def getTeacherMailBody(self):
        return MIMEText(graderMail, 'html')

    def getUniversityRelationsFollowUp(self, first_Name, company):
        return MIMEText(followUpBody2.format(
        firstName = first_Name,
        companyName = company
        ), 'html')

    def send(self, contacts, output):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        BASE_PATH = pathlib.Path().resolve()

        # for first_Name, last_Name, company, email, Position in contacts:
        for first_Name, company, email, Position, askingfor in contacts:
            mail = MIMEMultipart('alternative')
            mail['Subject'] = SUBJECT
            mail['From'] = self.sender_mail
            mail['To'] = email
            resumeFileName = "Amey_Bhilegaonkar_Resume.pdf"
            MSTxcptsFileName = "Amey_Bhilegaonkar_Masters_Grades.pdf"
            BETxcptsFileName = "Amey_Bhilegaonkar_Bachelors_Grades.pdf"
            if askingfor == "referral":
                text_content = self.getInternalReferalContent(first_Name, company, Position)

                # ATTACH RESUME WITH EMAIL

                Resume_File_Path = os.path.join(BASE_PATH, FILE_FOLDER, RESUME_FOLDER, Position, RESUME_FILE_NAME)
                self.attachDocument(mail, Resume_File_Path, resumeFileName)

            elif askingfor == "folloupUniv":
                text_content = self.getUniversityRelationsFollowUp(first_Name, company)
                # print(text_content)

            elif askingfor == "grader":
                text_content = self.getTeacherMailBody()
                # attach resume
                Resume_File_Path = os.path.join(BASE_PATH, FILE_FOLDER, RESUME_FOLDER, Position, RESUME_FILE_NAME)
                self.attachDocument(mail, Resume_File_Path, resumeFileName)

                # attach transcripts
                ms_txpts_File_Path = os.path.join(TRANSCRIPTS_FOLDER, MS_TRANSCRIPTS_NAME)
                self.attachDocument(mail, ms_txpts_File_Path, MSTxcptsFileName)

                # attach transcripts
                be_txpts_File_Path = os.path.join(TRANSCRIPTS_FOLDER, BE_TRANSCRIPTS_NAME)
                self.attachDocument(mail, be_txpts_File_Path, BETxcptsFileName)

                # print(text_content)

            else:
                print("Erroring out..")
                exit(-1)
            mail.attach(text_content)



            # CHECK IF WE ALREADY SENT AN EMAIL OR NOT
            if not self.checkInFile(email, output):
                service.sendmail(self.sender_mail, email, mail.as_string())
                self.writeToOutputFile(first_Name, email, output, askingfor)
            else:
                print(f"Skipping {email}")

        service.quit()
