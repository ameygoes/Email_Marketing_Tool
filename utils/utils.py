'''
-----------------------------------------------------------------------
File: utils.py
Creation Time: Nov 21st 2023 4:06 am
Author: Amey Bhilegaonkar
Developer Email: amey.bhilegaonkar@asu.edu
Copyright (c) 2023 Amey Bhilegaonkar. All rights reserved | GitHub: ameygoes
-----------------------------------------------------------------------
'''
from datetime import datetime
import yaml 
import os

def getCurrentTime():
    return datetime.now()

def getTotalTime(totalSeconds):
    hours = int(totalSeconds // 3600)
    minutes = int((totalSeconds % 3600) // 60)
    seconds = int(totalSeconds % 60)
    return hours, minutes, seconds


def readYML(filepath):
    # Load the YAML file
    with open(filepath, "r") as f:
        data = yaml.safe_load(f)

    return data

def readConfigurations(filepath):
    
    data = readYML(filepath)

    # Retrieve the values of first_name and last_name from the loaded data
    first_name = data['personal_details']['first_name']
    last_name = data['personal_details']['last_name']

    # Perform variable substitution in the YAML data
    data['resume_file_name'] = data['resume_file_name'].replace("{{ first_name }}", first_name)
    data['resume_file_name'] = data['resume_file_name'].replace("{{ last_name }}", last_name)
    data['cover_letter_file_name'] = data['cover_letter_file_name'].replace("{{ first_name }}", first_name)
    data['cover_letter_file_name'] = data['cover_letter_file_name'].replace("{{ last_name }}", last_name)
    data['ms_transcripts_name'] = data['ms_transcripts_name'].replace("{{ first_name }}", first_name)
    data['ms_transcripts_name'] = data['ms_transcripts_name'].replace("{{ last_name }}", last_name)
    data['be_transcripts_name'] = data['be_transcripts_name'].replace("{{ first_name }}", first_name)
    data['be_transcripts_name'] = data['be_transcripts_name'].replace("{{ last_name }}", last_name)

    # Print the updated data
    return data


def rename_files(folder_path, new_file_name):
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(old_file_path, new_file_path)    


# ATTACH FILE TO MAIL 
def attachDocument(self, mail, folder_path, fname):

    file_list = os.listdir(folder_path)

    # Filter PDF files
    pdf_files = [file for file in file_list if file.lower().endswith('.pdf')]

    # Attach each PDF file to an email
    for pdf_file in pdf_files:
        attachment_path = os.path.join(folder_path, pdf_file)

        mimeBase = MIMEBase("application", "octet-stream")
        with open(attachment_path, "rb") as file:
            mimeBase.set_payload(file.read())
        encoders.encode_base64(mimeBase)
        mimeBase.add_header("Content-Disposition", f"attachment; filename={fname}")
        mail.attach(mimeBase)