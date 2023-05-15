from configs.config import *
from configs.dbConfig import FETCH_RECRUITERS_TO_WHOM_EMAIL_WAS_NOT_SEND, FETCH_RECRUITERS_TO_WHOM_EMAIL_WAS_SENT_3_WEEKS_AGO
from configs.envrinomentSpecificConfgis import TABLE_NAME
from entity.hr_mail_pojo import HR_mail_pojo
from mail import Mail
from utils.dbUtils.dbUtils import readSQLQueryinPD
import yaml
import io

from utils.utils import readConfigurations
mailingList = []

def getSQLCommand(num):
    if num==1:
        return FETCH_RECRUITERS_TO_WHOM_EMAIL_WAS_NOT_SEND.format(TABLE_NAME)
    else:
        return FETCH_RECRUITERS_TO_WHOM_EMAIL_WAS_SENT_3_WEEKS_AGO.format(TABLE_NAME)
    
def main():
    sqlRcrdsDF = readSQLQueryinPD(getSQLCommand(1))
    
    
    for index, row in sqlRcrdsDF.iterrows():
        mail_agent = Mail()
        HR = HR_mail_pojo()
        HR.FirstName = row['FirstName']
        HR.LastName = row['LastName']
        HR.Email = row['Email']
        HR.Company = row['Company']
        HR.FirstEmailSentOn = row['FirstEmailSentOn']
        HR.FollowedUpOn = row['FollowedUpOn']
        # print(HR)
        # Access each element in the row using row[column_name] or row[column_index]


    
        mail_agent.send(HR)


configs = readConfigurations()

print(configs['ms_transcripts_name'])





