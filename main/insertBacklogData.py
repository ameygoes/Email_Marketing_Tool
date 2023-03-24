from entity.hr_mail_pojo import HR_mail_pojo

filePaths = ["..\output\mailingOutput.txt",
             "..\output\grader\mailingOutput.txt"]


def fillBacklogDataFromFile(filePath):
    with open(filePath) as f:
        lines = [line for line in f if line.strip()]

    for line in lines:
        hrMail = HR_mail_pojo()
        infoList = line.split(",")
        hrMail.FirstName = infoList[0]
        hrMail.LastName = infoList[1]
        hrMail.Email = infoList[2]
        hrMail.Company = infoList[2].split("@")[1].split(".")[0]
        hrMail.SentFor = infoList[3].split(" ")[2]
        hrMail.FirstEmailSentOn = infoList[3].split(" ")[4]
        hrMail.LinkedinProfile = None
        if (hrMail.SentFor == 'grader'):
            hrMail.IsProfessor = True
            hrMail.SentFor = "Grader Application"
        else:
            hrMail.IsProfessor = False
            hrMail.SentFor = "Internship - DE"
        hrMail.insertObjectInDBHr()


for filePath in filePaths:
    fillBacklogDataFromFile(filePath)
