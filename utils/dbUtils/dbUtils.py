import mysql.connector as mysqlConnector
from configs.dbConfig import CHECK_IF_EXISTS_IN_APOLLO, HOST_NAME, DB_NAME, DB_USER_NAME, INSERT_APOLO_POJO, PORT_NAME, DB_PASSWORD, CHECK_IF_EXISTS
from utils.constants import SQL_FILE_PREFIX
from utils.osUtils.osUtils import getOSPath, getBaseDir
from configs.envrinomentSpecificConfgis import APOLLO_TABLE_NAME, TABLE_NAME
import os
import datetime
import pandas as pd

BASE_DIR = getBaseDir()
# RETURN ERROR DETAILS STRING FOR LOGGING


def getErrorDetails(errorObject):
    return "{} \n {} \n {} \n {}".format(
        "Exception Occurred while Operating on Database: {}".format(
            errorObject),
        "Error Code: {}".format(errorObject.errno),
        "SQL_STATE: {}".format(errorObject.sqlstate),
        "Error Message: {}".format(errorObject.msg)
    )


def getSQLConnection():
    return mysqlConnector.connect(
        host=HOST_NAME,
        user=DB_USER_NAME,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        port=PORT_NAME
    )

# EXECUTE INSERT COMMAND
def executeCommand(command):
    # Open SQL Connection
    sqlConnector = getSQLConnection()

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



def executeCommand2(command, vals):
    # Open SQL Connection
    sqlConnector = getSQLConnection()

    mySQLCursor = sqlConnector.cursor()
    try:
        
        mySQLCursor.execute(CHECK_IF_EXISTS.format(TABLE_NAME), (vals[2],))
        result = mySQLCursor.fetchone()[0]
        if result == 0:
            mySQLCursor.execute(command, vals)

            # Insert into DB
            sqlConnector.commit()
            # print("Inserted!!")
        else:
            # pass
            print(f"Record with email: {vals[2]} already exists, skipping!")
        
    except mysqlConnector.Error as err:
        print(command)
        print(getErrorDetails(err))

    # Close the Connection
    mySQLCursor.close()
    sqlConnector.close()

def record_exists(sqlConnector, employee_id):
    cursor = sqlConnector.cursor()
    cursor.execute(CHECK_IF_EXISTS_IN_APOLLO.format(APOLLO_TABLE_NAME), (employee_id,))
    result = cursor.fetchone()
    return result[0] > 0

def executeMany(apolo_data):

    sqlConnector = getSQLConnection()
    mySQLCursor = sqlConnector.cursor()

    for employee in apolo_data:
        if not record_exists(sqlConnector, employee.get_id()):
            data = (employee.get_id(), employee.get_first_name(), employee.get_last_name(),
                    employee.get_linkedin_url(), employee.get_title(), employee.is_email_verified(),
                    employee.get_country(), employee.get_email(), employee.get_headline(),
                    employee.get_organization_name())

            try:
                mySQLCursor.execute(INSERT_APOLO_POJO.format(APOLLO_TABLE_NAME), data)
                sqlConnector.commit()
            except mysqlConnector.Error as err:
                print(getErrorDetails(err))
    
       
    # Close the Connection
    mySQLCursor.close()
    sqlConnector.close()

# EXECUTE GET COMMAND
def executeGetCommand(command):
    # Open SQL Connection
    returnOneRow = None
    
    sqlConnector = getSQLConnection()

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



def selectQuery(query):

    sqlConnector = mysqlConnector.connect(
        host=HOST_NAME,
        user=DB_USER_NAME,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        port=PORT_NAME
    )

    mySQLCursor = sqlConnector.cursor()

    mySQLCursor.execute(query)
    exists = mySQLCursor.fetchone()
    print(type.exists)
    mySQLCursor.close()
    sqlConnector.close()

    print(exists)
    if exists:
        return True
    return False


# EXECUTE TABLE CREATION
def createDBBootUp(fileNameList):
    print("=======================================================================================")
    # print(selectQuery(CHECK_DB.format(DB_NAME)))
    # if not selectQuery(CHECK_DB.format(DB_NAME)) or not selectQuery(CHECK_TABLE.format(TABLE_NAME)) or not selectQuery(CHECK_TABLE.format(TEST_TABLE_NAME)):
    for fileName in fileNameList:
        FullFilePath = os.path.join(BASE_DIR, SQL_FILE_PREFIX, fileName)
        FullFilePath = getOSPath(FullFilePath)
        print("Executing File: {}".format(FullFilePath))
        executeSQLFile(FullFilePath)
    # else:
        print("We already have table and db setup in the DataBase.")



def readSQLQueryinPD(command):
# Connect to the database
    sqlConnector = mysqlConnector.connect(
        host=HOST_NAME,
        user=DB_USER_NAME,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        port=PORT_NAME
    )

    # Read the query results into a pandas DataFrame
    df = pd.read_sql_query(command, con=sqlConnector)

    sqlConnector.close()

    return df
