from datetime import datetime
import yaml 


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