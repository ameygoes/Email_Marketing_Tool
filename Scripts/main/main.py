import csv
from configs.config import *
from main.mail import Mail
from entity.hr_mail_pojo import HR_mail_pojo
READ_URL = f"./{FILE_FOLDER}/{FILE_NAME}"
OUT_URL = f"./{OUTPUT_FOLDER}/{ASKING_FOR}/{OUTPUT_FILE}"

mailingList = []

def main(sending_Mail_for):
    with open(READ_URL) as csv_file:

        # READ CSV FILE
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        
        # TOTAL NUMBER OF MAILS TO BE SENT AND IGNORE HEADER
        count = 0
        row_tuple = ()
        # A ROW SHOULD HAVE - FIRSTNAME, COMPANY, EMAIL, POSITION_APPLYING_FOR, LINKEDIN_PROFILE, 
        for row in csv_reader:
            if count == 0:
                print("Reading Heading")
            else:
                # CREATE NEW HR_MAIL_OBJECT_FOR_EVERY_ROW
                objectPojo = HR_mail_pojo()

                row_tuple.add(row[0])
                row_tuple.add(row[1])
                row_tuple.add(row[2].strip())
                row_tuple.add(row[3])
                if sending_Mail_for.lower() == "grader":
                    row_tuple.add("grader")
                    row_tuple.add("NO_PROFILE")
                mailingList.append(row_tuple)
            count+=1


    mail_agent = Mail()
    mail_agent.send(mailingList, OUT_URL)
