# SYSTEM IMPORTS
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import pandas as pd
import os
import pathlib

# USER IMPORTS
from email import encoders
from config import *
from email_config import *


# DEFINE ROOT PATH
BASE_PATH = pathlib.Path().resolve()

# GET INPUT DATA FILE PATH
CSV_FILE_PATH = os.path.join(BASE_PATH, FILE_FOLDER, FILE_NAME)
df = pd.read_csv(CSV_FILE_PATH, header=0)

# LOOP OVER THE FILE AND SEND EMAIL TO EVERYONE
for index in df.index:

    # GET DESIRED FIELDS FROM FILE ROW BY ROW
    firstName =df['FirstName'].iloc[index]
    lastName =df['LastName'].iloc[index]
    email =df['Email'].iloc[index]
    company_Name =df['CompanyName'].iloc[index]
    gender = df['Gender'].iloc[index]
    Position = df['Position'].iloc[index]


    """
    THIS BLOCK IS FOR EMAIL BODY
    """
    # Create the body of the msg (a plain-text and an HTML version).
    text = INTERN_REFERAL.format(
    proNoun = PRONOUNS[gender.upper()],
    firstName = firstName,
    lastName = lastName,
    aspiring_role_title = SKILL_SET[Position]["LOOKING_TITLE"],
    companyName = company_Name,
    roleTitle = SKILL_SET[Position]["TITLE"],
    natural_interests = SKILL_SET[Position]["NATURAL_INTERESTS"],
    profesional_skills = SKILL_SET[Position]["SKILLS"],
    personalDetails=PERSONAL_DETAILS
    )
    # print(text)

    # CONVERT THE TEXT BODY INTO MIME OBJECT
    textPart = MIMEText(text, 'plain')

    # UNCOMMENT THIS PART TO ADD EMAIL SIGNATURE
    """
    THIS BLOCK IS HTML SIGN PART OF AN EMAIL
    """
    htmlPart = MIMEText(email_Sign, 'html')


    """
    THIS PART IS FOR EMAIL OBJECT CREATION AND SENDING PURPOSE
    """
    # msg = EmailMessage()
    # msg.set_content(textPart, subtype="plain")

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = email
    msg.attach(textPart)
    msg.attach(htmlPart)

    """
    THIS PART IS TO ATTACH AN RESUME AND COVER LETTER
    """
    # used to name attachment that's it
    pdfname = "Amey_Bhilegaonkar_Resume.pdf"
    cvname = "Amey_Bhilegaonkar_CV.pdf"

    Resume_File_Path = os.path.join(BASE_PATH, FILE_FOLDER, RESUME_FOLDER, Position, RESUME_FILE_NAME)
    # Cover_Letter_Path = os.path.join(BASE_PATH, FILE_FOLDER, RESUME_FOLDER, Position, COVER_LETTER_FILE_NAME)

    # open the file in bynary
    binary_pdf = open(Resume_File_Path, 'rb')
    PDFpayload = MIMEBase('application', 'octate-stream', Name=pdfname)
    PDFpayload.set_payload((binary_pdf).read())
    # enconding the binary into base64
    encoders.encode_base64(PDFpayload)
    # add header with pdf name
    PDFpayload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    msg.attach(PDFpayload)

    # # UNCOMMENT BELOW PART TO SEND COVER LETTER AS WELL ALONG WITH RESUME
    # binary_cv = open(Cover_Letter_Path, 'rb')
    # CVpayload = MIMEBase('application', 'octate-stream', Name=cvname)
    # CVpayload.set_payload((binary_cv).read())
    # encoders.encode_base64(CVpayload)
    # CVpayload.add_header('Content-Decomposition', 'attachment', filename=cvname)
    # msg.attach(CVpayload)


    try:
        # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(FROM, gmail_password)
        server.sendmail(FROM, email, msg.as_string())
        server.quit()

        print('Email sent to {}!'.format(email))
    except Exception as e:
        print(e.trace())
