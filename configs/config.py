from configs.envrinomentSpecificConfgis import CONFIGURATION_FILE
from utils.utils import readConfigurations

# READS THE CONFIGURATION FILE
configs = readConfigurations(CONFIGURATION_FILE)


USER_FIRST_NAME = configs['personal_details']['first_name']
USER_LAST_NAME = configs['personal_details']['last_name']
USER_GITHUB_URL = configs['personal_details']['github_url']
USER_PORTFOLIO_URL = configs['personal_details']['portfolio_url']
USER_CERTIFICATION_URL = configs['personal_details']['certification_url']
USER_SOFT_SKILLS = configs['personal_details']['soft_skills']

# THIS DEFINES NUMBER OF EMAIL ADDRESSES THAT A PERSON HAS
NUMBER_OF_EMAIL_ADDRESSES = configs['personal_details']['no_of_emails']

# THIS DEFINES YOUR MAIN FOLDER AFTER THE ROOT ATTACHMENT_FOLDER
# ROOT FOLDER IS WHERE YOUR SENDEMAILUSINGGMAIL SCRIPT IS LOCATED
ATTACHMENT_FOLDER = configs['attachments_folder'] 
RESUME_FOLDER = configs['resume_folder'] 
COVER_LETTER_FOLDER = configs['cover_letter_folder'] 
TRANSCRIPTS_FOLDER = configs['transcripts_folder'] 
MS_FOLDER = configs['ms_folder'] 
BE_FOLDER = configs['be_folder'] 

# THIS IS YOUR FILE NAME OF RESUME AND COVERLETTER
RESUME_FILE_NAME = configs['resume_file_name'] 
COVER_LETTER_FILE_NAME = configs['cover_letter_file_name'] 
MS_TRANSCRIPTS_NAME = configs['ms_transcripts_name'] 
BE_TRANSCRIPTS_NAME = configs['be_transcripts_name'] 

ATTACH_RESUME = configs['attach_resume'] 
ATTACH_COVER_LETTER = configs['attach_cover_letter'] 
ATTACH_MS_TRANSCRIPTS = configs['attach_ms_transcripts'] 
ATTACH_BS_TRANSCRIPTS = configs['attach_bs_transcripts'] 




# THIS DEFINES WHOM TO SEND EMAILS
FETCH_RECRUITERS = configs['fetch_recruiters'] 
FETCH_DEVELOPERS = configs['fetch_developers'] 
FETCH_TEACHERS = configs['fetch_teachers'] 
SEND_FOLLOW_UP = configs['send_follow_up'] 
SEND_THANK_YOU = configs['send_thank_you'] 

# THIS DEFINES IF YOU WANT TO SEND EMAILS TO SPECIFIC COMPANIES
SEND_EMAILS_TO_SPECIFIC_COMPANIES = configs['send_to_specific_company']
GET_COMPANY_NAME = configs['company_name']

# APPLYING FOR?
APPLYING_FOR = configs['applying_for']

# SKILL SET DICTINARY DEFINES A CERTAIN VALUES DEPENDING ON THE JOB TITLE YOU WANT TO APPLY FOR
# THE KEY FOR THE DICTIONARY COMES FROM THE INPUT CSV FILE - COL - POSITION
# WE ALSO NEED TO MAKE SURE WE HAVE THE SIMILAR FOLDER STRUCTURE FOR DATA LIKE RESUME AND CV ALSO
# SKILLS
SKILL_SET = configs['skill_set']
