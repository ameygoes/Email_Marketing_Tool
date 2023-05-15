import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pathlib
from configs.config import *
from configs.email_bodies import INTERN_REFERAL
from configs.email_config import *
from configs.dbConfig import *
from datetime import datetime as dt
from configs.envrinomentSpecificConfgis import TABLE_NAME
import random
from utils.dbUtils.dbUtils import executeCommand, executeGetCommand
class Mail:

    # INIT CONNECTION PARAMETERS 
    def __init__(self):
        random_number = random.randint(1,3)
        self.port = SMTP_PORT
        self.smtp_server_domain_name = SMTP_DOMAIN_NAME
        self.sender_mail = os.environ.get(FROM.format(random_number))
        self.password = os.environ.get(EMAIL_PASS.format(random_number))
        self.sent_for = "Iternship Search"
        self.position = "DATA"


    def __repr__(self) -> str:
        return self.sender_mail

    # CHECK IF EMAIL PRESENT IN DB?
    def checkIfRecordPresentInDB(self,email_to_search):
        return executeGetCommand(SEARCH_QUERY.format(TABLE_NAME, "Email", email_to_search))

    # ATTACH FILE TO MAIL 
    def attachDocument(self, mail, file_Path, fname):
        mimeBase = MIMEBase("application", "octet-stream")
        with open(file_Path, "rb") as file:
            mimeBase.set_payload(file.read())
        encoders.encode_base64(mimeBase)
        mimeBase.add_header("Content-Disposition", f"attachment; filename={fname}")
        mail.attach(mimeBase)

    # UPDATE DATABASE / INSERT A ROW IN DATABASE
    def makeUpdateToDB(self, HR):
        today = dt.now()
        if not HR.FollowedUpOn:
            executeCommand(UPDATE_QUERY_STR.format(TABLE_NAME, UPDATE_COL_2, today, HR.Email))
            executeCommand(UPDATE_QUERY_STR.format(TABLE_NAME, UPDATE_COL_4, self.sent_for, HR.Email))
        else:
            executeCommand(UPDATE_QUERY_STR.format(TABLE_NAME, UPDATE_COL_1, today, HR.Email))
            executeCommand(UPDATE_QUERY_STR.format(TABLE_NAME, UPDATE_COL_4, self.sent_for, HR.Email))
        # CHECK_IF_EMAIL_SENT_BEFORE.format(TABLE_NAME, HR.Email)

        print(f"Record timestamp was updated in DB for: {HR.Email}")

    def getInternalReferalContent(self, HR):
        return MIMEText(INTERN_REFERAL.format(
        firstName = HR.FirstName,
        # aspiring_role_title = SKILL_SET[Position]["LOOKING_TITLE"],
        companyName = HR.Company
        # roleTitle = SKILL_SET[Position]["TITLE"],
        # natural_interests = SKILL_SET[Position]["NATURAL_INTERESTS"],
        # profesional_skills = SKILL_SET[Position]["SKILLS"],
        # personalDetails=PERSONAL_DETAILS
        ), 'html')

    def getTeacherMailBody(self):
        return MIMEText(graderMail, 'html')

    def getUniversityRelationsFollowUp(self, first_Name, company):
        return MIMEText(followUpBody2.format(
        firstName = first_Name,
        companyName = company
        ), 'html')

    def send(self, HR):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        BASE_PATH = pathlib.Path().resolve()

        mail = MIMEMultipart('alternative')
        mail['Subject'] = SUBJECT_INTERNSHIP
        mail['From'] = self.sender_mail
        mail['To'] = HR.Email
        

        if self.position.lower() == "data":
            text_content = self.getInternalReferalContent(HR)

            # ATTACH RESUME WITH EMAIL
            Resume_File_Path = os.path.join(RESUME_FOLDER, RESUME_FILE_NAME)
            self.attachDocument(mail, Resume_File_Path, RESUME_FILE_NAME)

        elif self.sent_for.lower() == "folloupUniv":
            text_content = self.getUniversityRelationsFollowUp(HR.FirstName, HR.Company)
            # print(text_content)

        elif self.sent_for.lower() == "grader":
            text_content = self.getTeacherMailBody()
            # attach resume
            Resume_File_Path = os.path.join(BASE_PATH, FILE_FOLDER, RESUME_FOLDER, self.osition, RESUME_FILE_NAME)
            self.attachDocument(mail, Resume_File_Path, RESUME_FILE_NAME)

            # attach transcripts
            ms_txpts_File_Path = os.path.join(TRANSCRIPTS_FOLDER, MS_TRANSCRIPTS_NAME)
            self.attachDocument(mail, ms_txpts_File_Path, MS_TRANSCRIPTS_NAME)

            # # attach transcripts
            # be_txpts_File_Path = os.path.join(TRANSCRIPTS_FOLDER, BE_TRANSCRIPTS_NAME)
            # self.attachDocument(mail, be_txpts_File_Path, BETxcptsFileName)

            # print(text_content)

        else:
            print("Erroring out..")
            exit(-1)

        mail.attach(text_content)

        service.sendmail(self.sender_mail, HR.Email, mail.as_string())
        print(f"Email was sent to: {HR.Email}")
        self.makeUpdateToDB(HR)


        service.quit()
