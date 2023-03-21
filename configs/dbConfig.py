import os

DB_USER_NAME = "EMAIL_HR"
DB_PASSWORD = os.environ.get("EMAIL_HR_DB_PASS")
HOST_NAME = "localhost"
DB_NAME = "EMAIL_JOBS"
PORT_NAME = "3306"
PROD_TABLE_NAME = "HR_DETAILS"
TEST_TABLE_NAME = "TEST_HR_DETAILS"


SEARCH_QUERY = "SELECT id FROM {} WHERE {} = '{}'"
CHECK_DB = "SHOW DATABASES LIKE '{}'"
CHECK_TABLE = "SHOW TABLES LIKE '{}'"
INSERT_QUERY = "INSERT INTO {} VALUES('{}', '{}', '{}', '{}', {}, {}, '{}', {}, {})"
# INSERT_QUERY_htr = 'INSERT INTO %s ("FirstName","LastName","Email","Company","LinkedinProfile","IsProfessor","SentFor","FirstEmailSentOn","FollowedUpOn") VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
INSERT_QUERY_htr = "INSERT INTO `{}` (`FirstName`, `LastName`, `Email`, `Company`, `LinkedinProfile`, `IsProfessor`, `SentFor`, `FirstEmailSentOn`, `FollowedUpOn`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
UPDATE_QUERY_STR = "UPDATE {} SET {} = '{}'"
UPDATE_QUERY_NON_STR = "UPDATE {} SET {} = {}"
