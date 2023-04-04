from LinkedinScripts.GetLinkedInProfilesFromGoogle import GetLinkedinProfileLink
from configs.dbConfig import GET_HR_NULL_LINKEDIN, UPDATE_COL_3, UPDATE_QUERY_STR
from configs.envrinomentSpecificConfgis import TABLE_NAME
from utils.dbUtils.dbUtils import executeCommand, readSQLQueryinPD
import random as rand, time

def randomSleep():
    time.sleep(rand.randint(1,5))

lkProfilesDF = readSQLQueryinPD(GET_HR_NULL_LINKEDIN.format(TABLE_NAME))

lkProfile = GetLinkedinProfileLink()

for index, row in lkProfilesDF.iterrows():
    firstName = row["FirstName"]
    lastName = row["LastName"]
    company = row["Company"]
    email = row["Email"]

    
    lkProfileLink = lkProfile.getLinkedInProfile(firstName,lastName,company)

    if lkProfileLink:
        try:
            executeCommand(UPDATE_QUERY_STR.format(TABLE_NAME, UPDATE_COL_3, lkProfileLink, email))
            randomSleep()
            print("Profile Updated in DB")
        except:
            print("Failed to Update Profile in DB")
            
    else:
        print("Profile Not Found")