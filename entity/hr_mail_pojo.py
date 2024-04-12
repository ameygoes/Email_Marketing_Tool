from configs.dbConfig import INSERT_QUERY, INSERT_QUERY_htr
from configs.envrinomentSpecificConfgis import TABLE_NAME
from configs.dbConfig import UPDATE_QUERY_STR
from utils.dbUtils.dbUtils import executeCommand, executeCommand2


class HR_mail_pojo():

    # CONSTRUCTOR
    def __init__(self):
        self.FirstName = None
        self.LastName = None
        self.Email = None
        self.Company = None
        self.LinkedinProfile = None
        self.IsProfessor = False
        self.SentFor = None
        self.FirstEmailSentOn = None
        self.FollowedUpOn = None
        self.IsRecruiter = None
        self.IsDeveloper = None
        self.DidSend = None

    def __repr__(self):
        return f"Email is being Sent to: {self.FirstName} - {self.Email}"

    @staticmethod
    def getObjectValueList(listOfObjects):
        values = []
        for obj in listOfObjects:
            values.append((obj.FirstName, obj.LastName, obj.Email, obj.Company, obj.LinkedinProfile,
                  obj.IsProfessor, obj.IsRecruiter,obj.IsDeveloper,obj.DidSend, obj.SentFor, obj.FirstEmailSentOn, obj.FollowedUpOn))
        return values


    # INSERT OBJECT INTO DB
    def insertObjectInDB(self):
        print(INSERT_QUERY.format(
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
        ))
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

    @staticmethod
    def insertObjectInDBHr(listOfObjects):
        values = HR_mail_pojo.getObjectValueList(listOfObjects)
        for val in values:
            executeCommand2(INSERT_QUERY_htr.format(TABLE_NAME), val)


    # UPDATE RECORD IN DB
    def updateRecordInDB(self, COL_UPDATED, VALUE, STR_FLAG=False):
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
