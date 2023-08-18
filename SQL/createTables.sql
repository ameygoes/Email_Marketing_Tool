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

CREATE TABLE IF NOT EXISTS apolo_db_test (
    id varchar(255) PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    linkedin_url VARCHAR(255),
    title VARCHAR(255),
    email_status VARCHAR(50),
    country VARCHAR(255),
    email VARCHAR(255),
    headline VARCHAR(255),
    organization_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS apolo_db (
    id varchar(255) PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    linkedin_url VARCHAR(255),
    title VARCHAR(255),
    email_status VARCHAR(50),
    country VARCHAR(255),
    email VARCHAR(255),
    headline VARCHAR(255),
    organization_name VARCHAR(255)
);
