import csv
from config import *
from mail import Mail

READ_URL = f"./{FILE_FOLDER}/{FILE_NAME}"
OUT_URL = f"./{OUTPUT_FOLDER}/{OUTPUT_FILE}"

mailingList = []
with open(READ_URL) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0

    for row in csv_reader:
        if count == 0:
            print("Reading Heading")
        else:
            mailingList.append((row[0], row[1], row[2].strip(), row[3], ASKING_FOR))
        count+=1


mail_agent = Mail()
mail_agent.send(mailingList, OUT_URL)
