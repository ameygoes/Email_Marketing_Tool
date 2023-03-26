from configs.config import ENVIRONMENT, ASKING_FOR
from configs.dbConfig import TEST_TABLE_NAME, PROD_TABLE_NAME
import os 

if ENVIRONMENT.lower() == 'prod':
    TABLE_NAME = PROD_TABLE_NAME
    filePaths = ["..\output\mailingOutput.txt",
             "..\output\grader\mailingOutput.txt"]
    directory_path = "../Input/prod"
    TRUNCATE_MODE = False
else:
    TABLE_NAME = TEST_TABLE_NAME
    TRUNCATE_MODE = True
    filePaths = [os.path.join("..", "Input", "test", "mailingOutput.txt")]
        # Define the directory path
    directory_path = "../Input/test"

# if ASKING_FOR.lower() == 'grader':
