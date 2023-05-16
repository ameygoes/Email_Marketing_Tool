from configs.config import ENVIRONMENT
from configs.dbConfig import TEST_TABLE_NAME, PROD_TABLE_NAME
import os 

if ENVIRONMENT.lower() == 'prod':
    TABLE_NAME = PROD_TABLE_NAME
    filePaths = ["..\output\mailingOutput.txt",
             "..\output\grader\mailingOutput.txt"]
    directory_path = "../Input/prod"
    TRUNCATE_MODE = False
    CONFIGURATION_FILE = "../environment/prod.yml"

else:
    TABLE_NAME = TEST_TABLE_NAME
    TRUNCATE_MODE = False
    filePaths = [os.path.join("..", "Input", "test", "mailingOutput.txt")]
    directory_path = "../Input/test"
    CONFIGURATION_FILE = "../environment/test.yml"

