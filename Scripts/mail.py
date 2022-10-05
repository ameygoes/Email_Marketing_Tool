import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
import csv, pathlib
from config import *
from email_config import *
from datetime import date


class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "abhilega@asu.edu"
        self.password = gmail_password

    def checkInFile(self,search_word):
        file = open("mailingOutput")
        if(search_word in file.read()):
            return True
        else:
            return False

    def send(self, contacts, output):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        BASE_PATH = pathlib.Path().resolve()
        today = date.today()
        # for first_Name, last_Name, company, email, Position in contacts:
        for first_Name, company, email, Position in contacts:
            mail = MIMEMultipart('alternative')
            mail['Subject'] = 'Software Engineering Summer Internships 2023'
            mail['From'] = self.sender_mail
            mail['To'] = email
            text_content = MIMEText(INTERN_REFERAL.format(
            firstName = first_Name,
            # lastName = last_Name,
            aspiring_role_title = SKILL_SET[Position]["LOOKING_TITLE"],
            companyName = company,
            roleTitle = SKILL_SET[Position]["TITLE"],
            natural_interests = SKILL_SET[Position]["NATURAL_INTERESTS"],
            profesional_skills = SKILL_SET[Position]["SKILLS"],
            # personalDetails=PERSONAL_DETAILS
            ), 'html')

            mail.attach(text_content)
            # htmlPart = MIMEText(email_Sign, 'html')
            # mail.attach(htmlPart)

            pdfname = "Amey_Bhilegaonkar_Resume.pdf"

            Resume_File_Path = os.path.join(BASE_PATH, FILE_FOLDER, RESUME_FOLDER, Position, RESUME_FILE_NAME)
            mimeBase = MIMEBase("application", "octet-stream")
            with open(Resume_File_Path, "rb") as file:
                mimeBase.set_payload(file.read())
            encoders.encode_base64(mimeBase)
            mimeBase.add_header("Content-Disposition", f"attachment; filename={pdfname}")
            mail.attach(mimeBase)
            # print(self.checkInFile(email))
            if not self.checkInFile(email):
                service.sendmail(self.sender_mail, email, mail.as_string())
                # print(text_content)
                with open(output, mode='a') as employee_file:
                    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    employee_writer.writerow([first_Name, " ", email, f'Sent for {Position} on {today}'])
                print(f"Email Sent to: {email}")

        service.quit()
