import csv
from configs.config import *
from main.mail import Mail
from entity.hr_mail_pojo import HR_mail_pojo
from utils.dbUtils.dbUtils import readSQLQueryinPD


mailingList = []

def main(sending_Mail_for):
    df = readSQLQueryinPD(command)
    mail_agent = Mail()
    mail_agent.send(mailingList, OUT_URL)
