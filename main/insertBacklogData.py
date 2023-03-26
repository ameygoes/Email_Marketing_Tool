from configs.dbConfig import TRUNCATE_TABLE
from entity.hr_mail_pojo import HR_mail_pojo
import os
import pandas as pd
import sys
from configs.envrinomentSpecificConfgis import  *
from utils.dbUtils.dbUtils import executeCommand
mode = int(sys.argv[1])
print("Running")

def getFileList():
    fileList = []

    # Get a list of all files in the directory
    files = os.listdir(directory_path)
    # Loop through the files and print the names of text files
    for file in files:
        if file.endswith(".csv"):
            fileList.append(os.path.join(directory_path, file))
    return fileList

# INSERT FROM TEXT FILE
def fillBacklogDataFromFile(filePath):
    with open(filePath) as f:
        lines = [line for line in f if line.strip()]
    hrpojos = []
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
        hrpojos.append(hrMail)
    HR_mail_pojo.insertObjectInDBHr(hrpojos)

# INSERT FROM CSV FILE
def fillBacklogDataFromCSV(filePath, professorFlag, recruiterFlag, developerFlag):
    df = pd.read_csv(filePath)
    df = df.fillna('')
    # Loop through each row of the dataframe and create a HRPojo object for each row
    hrpojos = []
    for index, row in df.iterrows():
        hrpojo = HR_mail_pojo()
    
        hrpojo.FirstName = row['First Name']
        hrpojo.LastName = row['Last Name']
        hrpojo.Email = row['Email']
        hrpojo.Company = row['Company']
        hrpojo.LinkedinProfile = row['Person Linkedin Url']
        hrpojo.IsRecruiter = recruiterFlag
        hrpojo.IsProfessor = professorFlag
        hrpojo.IsDeveloper = developerFlag
        hrpojos.append(hrpojo)
    
    HR_mail_pojo.insertObjectInDBHr(hrpojos)

def InsertBackLogFromTXT():
    for filePath in filePaths:
        fillBacklogDataFromFile(filePath)

def InsertBackLogFromCSV(professorFlag, recruiterFlag, developerFlag):
    fileList = getFileList()
    for filePath in fileList:
        fillBacklogDataFromCSV(filePath, professorFlag, recruiterFlag, developerFlag)

if mode==0:

    if TRUNCATE_MODE:
        executeCommand(TRUNCATE_TABLE.format(TABLE_NAME))
    # PROFESSORS and RECRUITERS
    InsertBackLogFromTXT()
elif mode == 1:
    # RECRUITERS
    InsertBackLogFromCSV(False, True, False)
elif mode == 2:
    # #  PROFESSORS
    InsertBackLogFromCSV(True, False, False)
else:
    # # DEVELOPERS
    InsertBackLogFromCSV(False, False, True)
