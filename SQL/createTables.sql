CREATE DATABASE IF NOT EXISTS EMAIL_JOBS;
USE EMAIL_JOBS;
CREATE TABLE IF NOT EXISTS HR_DETAILS (
id int primary key auto_increment,
FirstName VARCHAR(250)  NOT NULL,
LastName VARCHAR(250),
Email VARCHAR(250)  NOT NULL,
Company VARCHAR(250)  NOT NULL,
LinkedinProfile VARCHAR(250),
IsProfessor boolean default False,
IsRecruiter boolean,
IsDeveloper boolean,
DidSend boolean,
SentFor VARCHAR(250) NOT NULL,
FirstEmailSentOn TIMESTAMP DEFAULT NULL,
FollowedUpOn TIMESTAMP default NULL
);

CREATE TABLE IF NOT EXISTS TEST_HR_DETAILS (
id int primary key auto_increment,
FirstName VARCHAR(250)  NOT NULL,
LastName VARCHAR(250),
Email VARCHAR(250)  NOT NULL,
Company VARCHAR(250)  NOT NULL,
LinkedinProfile VARCHAR(250),
IsProfessor boolean default False,
IsRecruiter boolean,
IsDeveloper boolean,
DidSend boolean,
SentFor VARCHAR(250) NOT NULL,
FirstEmailSentOn TIMESTAMP DEFAULT NULL,
FollowedUpOn TIMESTAMP default NULL
);
