import mysql.connector as mysqlConnector
from configs.dbConfig import HOST_NAME, DB_NAME, DB_USER_NAME, PORT_NAME, DB_PASSWORD, TABLE_NAME, TEST_TABLE_NAME
from utils.constants import SQL_FILE_PREFIX
from utils.osUtils.osUtils import getOSPath, getBaseDir

BASE_DIR = getBaseDir()
# RETURN ERROR DETAILS STRING FOR LOGGING
def getErrorDetails(errorObject):
    return "{} \n {} \n {} \n {}".format(
        "Exception Occurred while Operating on Database: {}".format(errorObject),
        "Error Code: {}".format(errorObject.errno),
        "SQL_STATE: {}".format(errorObject.sqlstate),
        "Error Message: {}".format(errorObject.msg)
    )


# EXECUTE INSERT COMMAND
def executeInsertCommand(command):
    # Open SQL Connection
    sqlConnector = mysqlConnector.connect(
        host=HOST_NAME,
        user=DB_USER_NAME,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        port=PORT_NAME
    )

    mySQLCursor = sqlConnector.cursor()

    try:
        # Execute Command
        mySQLCursor.execute(command)

        # Insert into DB
        sqlConnector.commit()

    except mysqlConnector.Error as err:
        print(getErrorDetails(err))

    # Close the Connection
    mySQLCursor.close()
    sqlConnector.close()


# EXECUTE GET COMMAND
def executeGetCommand(command):
    # Open SQL Connection
    sqlConnector = mysqlConnector.connect(
        host=HOST_NAME,
        user=DB_USER_NAME,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        port=PORT_NAME
    )

    mySQLCursor = sqlConnector.cursor()

    try:
        # Execute Command
        mySQLCursor.execute(command)

        # Fetch from Table and return one Row
        returnOneRow = mySQLCursor.fetchall()

    except mysqlConnector.Error as err:
        print(getErrorDetails(err))

    # Close the Connection
    mySQLCursor.close()
    sqlConnector.close()

    # Return one Row
    return returnOneRow


# EXECUTE TABLE CREATION
def executeSQLFile(SQLFilePath):
    # Open SQL Connection
    sqlConnector = mysqlConnector.connect(
        host=HOST_NAME,
        user=DB_USER_NAME,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        port=PORT_NAME
    )

    # READ SQL FILE AND EXECUTE IT
    try:
        with open(SQLFilePath, 'r') as fileObject:
            sqlScript = fileObject.read()
            for sqlStatements in sqlScript.split(";\n"):
                if sqlStatements == "":
                    continue
                else:
                    mySQLCursor = sqlConnector.cursor()
                    mySQLCursor.execute(sqlStatements)
                    sqlConnector.commit()
                    mySQLCursor.close()

    except mysqlConnector.Error as err:
        print(getErrorDetails(err))

    # Close the Connection
    sqlConnector.close()

def checkIfDBEXists(dbname):

    sqlConnector = mysqlConnector.connect(
        host=HOST_NAME,
        user=DB_USER_NAME,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        port=PORT_NAME
    )

    mySQLCursor = sqlConnector.cursor()

    mySQLCursor.execute("SHOW DATABASES LIKE '{}'".format(dbname))
    exists = mySQLCursor.fetchone()

    mySQLCursor.close()
    sqlConnector.close()

    if exists:
        return True
    return False

def checkIfTableEXists(tableName):

    sqlConnector = mysqlConnector.connect(
        host=HOST_NAME,
        user=DB_USER_NAME,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        port=PORT_NAME
    )

    mySQLCursor = sqlConnector.cursor()

    mySQLCursor.execute("SHOW TABLES LIKE '{}'".format(tableName))
    exists = mySQLCursor.fetchone()

    mySQLCursor.close()
    sqlConnector.close()

    if exists:
        return True
    return False


# EXECUTE TABLE CREATION
def createDBBootUp(fileNameList):

    if not checkIfDBEXists(DB_NAME) or not checkIfTableEXists(TABLE_NAME) or not checkIfTableEXists(TEST_TABLE_NAME):
        for fileName in fileNameList:
            FullFilePath = BASE_DIR + SQL_FILE_PREFIX + fileName
            FullFilePath = getOSPath(FullFilePath)
            print("Executing File: {}".format(FullFilePath))
            executeSQLFile(FullFilePath)
    else:
        print("we already have table and db setup in the DataBase.")