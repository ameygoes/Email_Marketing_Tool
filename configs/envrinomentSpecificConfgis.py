from configs.config import ENVIRONMENT, ASKING_FOR
from configs.dbConfig import TEST_TABLE_NAME, PROD_TABLE_NAME

if ENVIRONMENT.lower() == 'prod':
    TABLE_NAME = PROD_TABLE_NAME
else:
    TABLE_NAME = TEST_TABLE_NAME

# if ASKING_FOR.lower() == 'grader':
