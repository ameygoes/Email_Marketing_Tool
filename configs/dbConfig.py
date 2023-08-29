import os

DB_USER_NAME = "EMAIL_HR"
DB_PASSWORD = os.environ.get("EMAIL_HR_DB_PASS")
HOST_NAME = "localhost"
DB_NAME = "EMAIL_JOBS"
PORT_NAME = "3306"
PROD_TABLE_NAME = "HR_DETAILS"
TEST_TABLE_NAME = "TEST_HR_DETAILS"
PROD_APOLO = "apolo_db"
TEST_APOLO = "apolo_db_test"

SEARCH_QUERY = "SELECT id FROM {} WHERE {} = '{}'"
CHECK_DB = "SHOW DATABASES LIKE '{}'"
CHECK_TABLE = "SHOW TABLES LIKE '{}'"

INSERT_APOLO_POJO = "INSERT INTO {} (id, first_name, last_name, linkedin_url, title, email_status, country, email, headline, organization_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
INSERT_QUERY = "INSERT INTO {} VALUES('{}', '{}', '{}', '{}', {}, {}, '{}', {}, {})"
CHECK_IF_EXISTS =  "SELECT COUNT(*) FROM {} WHERE email = %s"
CHECK_IF_EXISTS_IN_APOLLO = "SELECT COUNT(*) FROM {} WHERE id = %s"
INSERT_QUERY_htr = "INSERT IGNORE  INTO `{}` (`FirstName`,`LastName`,`Email` ,`Company`,`LinkedinProfile`,`IsProfessor`,`IsRecruiter`,`IsDeveloper`,`DidSend`,`SentFor`,`FirstEmailSentOn`,`FollowedUpOn`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
UPDATE_QUERY_STR = "UPDATE {} SET {} = '{}' WHERE Email = '{}'"
UPDATE_QUERY_NON_STR = "UPDATE {} SET {} = {}"
TRUNCATE_TABLE = "TRUNCATE TABLE {}"
CHECK_IF_EMAIL_SENT_BEFORE = "SELECT COUNT(*) FROM {} WHERE EMAIL=`{}`"
UPDATE_COL_1 = "FollowedUpOn"
UPDATE_COL_2 = "FirstEmailSentOn"
UPDATE_COL_3 = "LinkedinProfile"
UPDATE_COL_4 = "SentFor"
UPDATE_COL_5 = ""
GET_HR_NULL_LINKEDIN = "SELECT `FirstName`, `LastName`, `Company`,`Email` FROM {} WHERE `LinkedinProfile` IS NULL AND IsProfessor = False"

# 
FETCH_RECRUITERS_TO_WHOM_EMAIL_WAS_NOT_SEND = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn  FROM {} WHERE IsRecruiter = True and FirstEmailSentOn IS NULL"
FETCH_RECRUITERS_TO_WHOM_EMAIL_WAS_SENT_3_WEEKS_AGO = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn FROM {} WHERE  IsRecruiter = True and FirstEmailSentOn <= DATE_SUB(NOW(), INTERVAL 3 WEEK) and FollowedUpOn IS NULL"
FETCH_RECRUITERS_FOLLOWED_UP_SENT_3_WEEKS_AGO = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn FROM {} WHERE  IsRecruiter = True and FollowedUpOn <= DATE_SUB(NOW(), INTERVAL 3 WEEK) and FollowedUpOn IS NOT NULL"
FETCH_RECRUITERS_TO_WHOM_EMAIL_WAS_NOT_SEND_FROM_A_COMPANY = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn  FROM {} WHERE IsRecruiter = True and FirstEmailSentOn IS NULL and company = {}"
FETCH_RECRUITERS_TO_WHOM_EMAIL_WAS_SENT_3_WEEKS_AGO_FROM_A_COMPANY = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn FROM {} WHERE  IsRecruiter = True and FirstEmailSentOn <= DATE_SUB(NOW(), INTERVAL 3 WEEK) and FollowedUpOn IS NULL and company = '{}'"


FETCH_DEVELOPER_TO_WHOM_EMAIL_WAS_NOT_SEND = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn FROM {} WHERE IsDeveloper = True and FirstEmailSentOn IS NULL"
FETCH_DEVELOPER_TO_WHOM_EMAIL_WAS_SENT_3_WEEKS_AGO = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn FROM {} WHERE  IsDeveloper = True and FirstEmailSentOn <= DATE_SUB(NOW(), INTERVAL 3 WEEK) and FollowedUpOn IS NULL"
FETCH_DEVELOPER_TO_WHOM_EMAIL_WAS_NOT_SEND_FROM_A_COMPANY = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn FROM {} WHERE IsDeveloper = True and FirstEmailSentOn IS NULL"
FETCH_DEVELOPER_TO_WHOM_EMAIL_WAS_SENT_3_WEEKS_AGO_FROM_A_COMPANY = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn FROM {} WHERE  IsDeveloper = True and FirstEmailSentOn <= DATE_SUB(NOW(), INTERVAL 3 WEEK) and FollowedUpOn IS NULL and company = '{}'"
FETCH_DEVELOPER_FOLLOWED_UP_SENT_3_WEEKS_AGO = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn FROM {} WHERE  IsDeveloper = True and FollowedUpOn <= DATE_SUB(NOW(), INTERVAL 3 WEEK) and FollowedUpOn IS NOT NULL and company = '{}'"


FETCH_TEACHERS_TO_WHOM_EMAIL_WAS_NOT_SEND = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn FROM {} WHERE IsProfessor = True and FirstEmailSentOn IS NULL"
FETCH_TEACHERS_TO_WHOM_EMAIL_WAS_SENT_3_WEEKS_AGO = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn FROM {} WHERE  IsProfessor = True and FirstEmailSentOn <= DATE_SUB(NOW(), INTERVAL 3 WEEK) and FollowedUpOn IS NULL"
FETCH_TEACHER_FOLLOWED_UP_SENT_3_WEEKS_AGO = "SELECT FirstName, LastName, Email, Company, FollowedUpOn, FirstEmailSentOn FROM {} WHERE  IsProfessor = True and FollowedUpOn <= DATE_SUB(NOW(), INTERVAL 3 WEEK) and FollowedUpOn IS NOT NULL"