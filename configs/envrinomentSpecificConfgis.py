from configs.runaable_configs import ENVIRONMENT
from configs.dbConfig import PROD_APOLO, TEST_APOLO, TEST_TABLE_NAME, PROD_TABLE_NAME
import os 

if ENVIRONMENT.lower() == 'prod':
    TABLE_NAME = PROD_TABLE_NAME
    APOLLO_TABLE_NAME = PROD_APOLO
    filePaths = ["..\output\mailingOutput.txt",
             "..\output\grader\mailingOutput.txt"]
    directory_path = "../Input/prod"
    TRUNCATE_MODE = False
    CONFIGURATION_FILE = "../environment/prod.yml"

else:
    TABLE_NAME = TEST_TABLE_NAME
    APOLLO_TABLE_NAME = TEST_APOLO
    TRUNCATE_MODE = False
    filePaths = [os.path.join("..", "Input", "test", "mailingOutput.txt")]
    directory_path = "../Input/test"
    CONFIGURATION_FILE = "../environment/test.yml"

