from utils.dbUtils import INSERT_QUERY
from configs.envrinomentSpecificConfgis import TABLE_NAME
from configs.dbConfig import UPDATE_QUERY_STR, UPDATE_QUERY
from utils.dbUtils import executeCommand
class HR_mail_pojo():
    
    # CONSTRUCTOR
    def __init__(self):
        self.FirstName = None,
        self.LastName  = None,
        self.Email  = None,
        self.Company = None,
        self.LinkedinProfile = None,
        self.IsProfessor = True,
        self.SentFor  = None,
        self.FirstEmailSentOn = None,
        self.FollowedUpOn = None

    # INSERT OBJECT INTO DB
    def insertObjectInDB(self):
        executeCommand(
                INSERT_QUERY.format(
                TABLE_NAME,
                self.FirstName,
                self.LastName,
                self.Email,
                self.Company,
                self.LinkedinProfile,
                self.IsProfessor,
                self.SentFor,
                self.FirstEmailSentOn,
                self.FollowedUpOn
            )
        )
    
    # UPDATE RECORD IN DB
    def updateRecordInDB(self, COL_UPDATED, VALUE, STR_FLAG = False):
        if not STR_FLAG:
            UPDATE_QUERY = UPDATE_QUERY
        else:
            UPDATE_QUERY = UPDATE_QUERY_STR

        executeCommand(
            UPDATE_QUERY.format(
            TABLE_NAME,
            COL_UPDATED,
            VALUE
            )
        )


