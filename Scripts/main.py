import csv

from mail import Mail

READ_URL = "./Data/MailingList.csv"
OUT_URL = "./mailingOutput"

mailingList = []
with open(READ_URL) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0

    for row in csv_reader:
        if count == 0:
            print("Reading Heading")
        else:
            mailingList.append((row[0], row[1], row[2].strip(), row[3])) #,row[4]))
        count+=1


mail_agent = Mail()

mail_agent.send(mailingList, OUT_URL)
