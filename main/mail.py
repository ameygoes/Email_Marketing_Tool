import sys
import random
from datetime import datetime as dt
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from configs.config import *
from configs.email_bodies import GRADER_MAIL, INTERN_REFERAL, SLIDING_INTO_DMS, THANK_YOU_EMAIL
from configs.email_config import *
from configs.dbConfig import *
from configs.envrinomentSpecificConfgis import TABLE_NAME

from utils.dbUtils.dbUtils import BASE_DIR, executeCommand, executeGetCommand

class Mail:

    # INIT CONNECTION PARAMETERS 
    def __init__(self):
        random_number = random.randint(1,NUMBER_OF_EMAIL_ADDRESSES)
        self.port = SMTP_PORT
        self.smtp_server_domain_name = SMTP_DOMAIN_NAME
        self.sender_mail = os.environ.get(FROM.format(random_number))
        self.password = os.environ.get(EMAIL_PASS.format(random_number))


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

    # GET EMAIL BODY FROM EMAIL_BODIES.PY
    def getEmailBody(self, HR):
        if FETCH_RECRUITERS:
            return INTERN_REFERAL.format(
                firstName = HR.FirstName,
                userFirstName = USER_FIRST_NAME,
                userLastName = USER_LAST_NAME,
                applying_for = APPLYING_FOR,
                companyName = HR.Company,
                userCertificationURL = USER_CERTIFICATION_URL,
                soft_skills = USER_SOFT_SKILLS,
                userPortFolioURL = USER_PORTFOLIO_URL,
                userGitHubURL = USER_GITHUB_URL  
            )
        
        elif FETCH_DEVELOPERS:
            return INTERN_REFERAL.format(
                firstName = HR.FirstName,
                userFirstName = USER_FIRST_NAME,
                userLastName = USER_LAST_NAME,
                applying_for = APPLYING_FOR,
                companyName = HR.Company,
                userCertificationURL = USER_CERTIFICATION_URL,
                soft_skills = USER_SOFT_SKILLS,
                userPortFolioURL = USER_PORTFOLIO_URL,
                userGitHubURL = USER_GITHUB_URL  
            )
        
        elif FETCH_TEACHERS:
            return GRADER_MAIL
        
        elif SEND_FOLLOW_UP:
             return SLIDING_INTO_DMS.format(
                 firstName = HR.FirstName,
                 userFirstName = USER_FIRST_NAME,
                 userLastName = USER_LAST_NAME,
                 userPortFolioURL = USER_PORTFOLIO_URL,
                 companyName = HR.Company,
             )
        
        elif SEND_THANK_YOU:
             return THANK_YOU_EMAIL.format(
                 firstName = HR.FirstName,
                 userFirstName = USER_FIRST_NAME,
                 userLastName = USER_LAST_NAME,
                 companyName = HR.Company
             )
        else:
            return sys.exit(1)
    
    # GET EMAIL BODY AS HTML
    def getEmailAsHTML(self, HR):
        return MIMEText(self.getEmailBody(HR), 'html')

    # ATTACH FILES TO MAIL SPECIFIED IN THE CONFIG FILE
    def attachNecessaryFiles(self, mail):
        if ATTACH_RESUME:
             resume_path = os.path.join(BASE_DIR, ATTACHMENT_FOLDER, RESUME_FOLDER, RESUME_FILE_NAME)
             self.attachDocument(mail, resume_path, RESUME_FILE_NAME)
        
        if ATTACH_COVER_LETTER:
            cover_letter_path = os.path.join(BASE_DIR, ATTACHMENT_FOLDER, COVER_LETTER_FOLDER, COVER_LETTER_FILE_NAME)
            self.attachDocument(mail, cover_letter_path, COVER_LETTER_FILE_NAME)

        if ATTACH_MS_TRANSCRIPTS:
            ms_transcripts_path = os.path.join(BASE_DIR, ATTACHMENT_FOLDER, TRANSCRIPTS_FOLDER, MS_TRANSCRIPTS_NAME)
            self.attachDocument(mail, ms_transcripts_path, MS_TRANSCRIPTS_NAME)

        if ATTACH_BS_TRANSCRIPTS:
            bs_transcripts_path = os.path.join(BASE_DIR, ATTACHMENT_FOLDER, TRANSCRIPTS_FOLDER, BE_TRANSCRIPTS_NAME)
            self.attachDocument(mail, bs_transcripts_path, BE_TRANSCRIPTS_NAME)


    def send(self, HR):

        # LOGIN
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.paslsword)
        
        # INITIATE
        mail = MIMEMultipart('alternative')
        mail['Subject'] = SUBJECT_INTERNSHIP
        mail['From'] = self.sender_mail
        mail['To'] = HR.Email
        
        # ATTACH FILES
        HTML_content = self.getEmailAsHTML(HR)
        self.attachNecessaryFiles(mail)
        mail.attach(HTML_content)

        # SEND
        service.sendmail(self.sender_mail, HR.Email, mail.as_string())
        print(f"Email was sent to: {HR.Email}")
        self.makeUpdateToDB(HR)
        service.quit()
