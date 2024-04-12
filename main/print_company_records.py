from configs.config import *
from configs.dbConfig import FETCH_PEOPLE_FROM_A_COMPANY, MAKE_DEV_READY
from configs.envrinomentSpecificConfgis import TABLE_NAME
from configs.runaable_configs import ENVIRONMENT
from entity.hr_mail_pojo import HR_mail_pojo
from utils.dbUtils.dbUtils import executeCommand, readSQLQueryinPD


def main():
    sqlRcrdsDF = readSQLQueryinPD(FETCH_PEOPLE_FROM_A_COMPANY.format(TABLE_NAME, GET_COMPANY_NAME))
    for index, row in sqlRcrdsDF.iterrows():
        HR = HR_mail_pojo()
        HR.FirstName = row['FirstName']
        HR.LastName = row['LastName']
        HR.Email = row['Email']
        HR.Company = row['Company'].capitalize()
        HR.FirstEmailSentOn = row['FirstEmailSentOn']
        HR.FollowedUpOn = row['FollowedUpOn']
        print(HR)

def make_dev_ready():
    if ENVIRONMENT.lower() != 'prod':
        executeCommand(MAKE_DEV_READY.format(TABLE_NAME, GET_COMPANY_NAME, TABLE_NAME))

make_dev_ready()