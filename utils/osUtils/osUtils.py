#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------

import os
import sys
import platform

from utils.constants import DEFAULT_OS, PROJECT, WINDOWS_SPLIT_PARAM, LINUX_SPLIT_PARAM

# GET CURRENT OPERATING SYSTEM
os_name = platform.system()


def getSplitParameter(osName):
    if osName.lower() != DEFAULT_OS.lower():
        return LINUX_SPLIT_PARAM
    else:
        return WINDOWS_SPLIT_PARAM


def getLinuxPath(DirectoryPath):
    DirectoryPath = DirectoryPath.replace("\\", "/")
    DirectoryPath = DirectoryPath.replace("\\\\", "/")
    return DirectoryPath


def getWindowsPath(DirectoryPath):
    DirectoryPath = DirectoryPath.replace("\\", "\\\\")
    DirectoryPath = DirectoryPath.replace("/", "\\\\")
    return DirectoryPath


def getOSPath(DirectoryPath):
    if os_name.lower() != DEFAULT_OS.lower():
        return getLinuxPath(DirectoryPath)
    else:
        return getWindowsPath(DirectoryPath)


def getBaseDir():
    BASE_DIR = ''
    flag = True
    for path in sys.path:
        possibleProjectName = path.split(getSplitParameter(os_name))[-1]
        if PROJECT.lower() == possibleProjectName.lower():
            BASE_DIR = path
            flag = False
            break

    if flag:
        print("Failed to SET BASE_DIR. Please follow Instructions from Helps/HowToGetStartedwithTNPProject.txt File")
    else:
        print("Your BASE_DIR is SET to: {} ".format(BASE_DIR))

    return BASE_DIR
