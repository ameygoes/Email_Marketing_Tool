#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------

import sys
import platform
import os
import argparse

from utils.constants import DEFAULT_OS, PTH_FILE_NAME, WINDOWS_PTH_FILE_PATH, LINUX_PATH_FILE_PATH, SQL_CREATE_FILE_NAMES
from utils.dbUtils.dbUtils import createDBBootUp
from utils.osUtils.osUtils import getLinuxPath, getWindowsPath

# Adding Parsers
parser = argparse.ArgumentParser(description='Get the flags for Adding Path File and Creating,Deleting or Do Nothing '
                                             'to the Tables')
parser.add_argument('--addPthFile', dest='addPthFile', type=str, help='Set True for Adding Project Path to SYS PATH '
                                                                      'Set False if you have already added it.')
# parser.add_argument('--setUpDB', dest='setUpDB', type=str, help='setUpDB takes three arguments -'
#                                                                 '1. Create - Used for Creating all necessary tables on the Machine.'
#                                                                 '2. Delete - Used for Deleting all necessary tables from Machine.'
#                                                                 '3. Nothing - Default Option to do Nothing.')
args = parser.parse_args()


def getBoolArgument(stringArgument):
    if stringArgument.lower() == "true":
        addPthFile = True
    elif stringArgument.lower() == "false":
        addPthFile = False
    else:
        addPthFile = None
    return addPthFile


# setUpDB = args.setUpDB
addPthFileFlag = getBoolArgument(args.addPthFile)
print(args)

if (addPthFileFlag is None): # or (setUpDB is None):
    print("Please provide Necessary Arguments")
    sys.exit(-1)


def executeSQL(FileNameList):
    print("Executing SQL Files: {}".format(FileNameList))
    try:
        createDBBootUp(FileNameList)
        print("All SQL Files were processed Successfully!")
    except Exception as exp:
        print("DataBase Booting up failed!!! Try Setting DataBase values in DataBaseProperties.py")
        print(exp)


if addPthFileFlag:
    # GET CURRENT OPERATING SYSTEM
    os_name = platform.system()

    # GET PYTHON VERSION INFORMATION
    pythonMajorVersion = sys.version_info.__getattribute__("major")
    pythonMinorVersion = sys.version_info.__getattribute__("minor")

    # GET PRESENT WORKING DIRECTORY - IDEALLY SHOULD BE THE FOLDER PATH
    # TO PROJECT BASE DIRECTORY
    currDirectory = os.getcwd()

    # CHECK IF THE OS IS WINDOWS OR NOT
    if os_name.lower() != DEFAULT_OS.lower():

        # IF ITS OTHER THAN WINDOWS, THEN PREPARE PATH OF LINUX
        currDirectory = getLinuxPath(currDirectory)
        filePathDestination = LINUX_PATH_FILE_PATH.format(pythonMajorVersion, pythonMinorVersion, PTH_FILE_NAME)

    else:
        # OTHERWISE, PREPARE PATH FOR WINDOWS
        currDirectory = getWindowsPath(currDirectory)

        # GET PRESENT USER IF ITS WINDOWS - IDEALLY SHOULD BE THE FOLDER PATH
        # TO PROJECT BASE DIRECTORY
        currUser = os.path.expanduser('~')
        filePathDestination = WINDOWS_PTH_FILE_PATH.format(currUser, pythonMajorVersion, pythonMinorVersion,
                                                           PTH_FILE_NAME)

        filePathDestination = getWindowsPath(filePathDestination)

    # CREATE A FILE WITH .PTH EXTENSIONS TO COPY IT TO SITE-PACKAGES
    f = open(filePathDestination, "w+")
    f.write(currDirectory)
    f.close()

    print("Pth file was added successfully to the path: {}".format(filePathDestination))

else:
    print("You have Opted not to add Pth File.")

# if setUpDB.lower() == "create":
executeSQL(SQL_CREATE_FILE_NAMES)
# else:
#     print("You have Opted not doing any changes to Tables in DB.")