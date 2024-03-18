import json 
import os



"""
What to do with Vue components?????????

Replace markdown.

ADD PATH AND NAME TO JSON FILES 

"""

def get_files_in_directory(path):
    files = os.listdir(path)
    return files

paths = [
    '../src/data/Classes/',
    '../src/data/CompSci/',
    '../src/data/jobs/',
    '../src/data/LinkedIn/',
    '../src/data/Other/',
]

all_functions_str = ""

for path in paths:

    for file_name in get_files_in_directory(path):
        file = file_name.replace(".json", "")
        
        if ".docx" not in file_name and ".vue" not in file_name:
            func_str = (f'def get_{file.lower()}():\n'
                        f'    with open("{path}{file_name}", "r") as file:\n'
                        '        content = json.load(file)\n\n')

        all_functions_str += func_str


home_str = ('def get_home():\n'
           f'    with open("../src/data/Home.json", "r") as file:\n'
            '        content = json.load(file)\n\n')

all_functions_str += home_str

print(all_functions_str.strip())


def get_classestoavoid():
    with open("../src/data/Classes/ClassesToAvoid.json", "r") as file:
        content = json.load(file)

def get_classrecommendations():
    with open("../src/data/Classes/ClassRecommendations.json", "r") as file:
        content = json.load(file)

def get_usefulcertifications():
    with open("../src/data/Classes/UsefulCertifications.json", "r") as file:
        content = json.load(file)

def get_cscdescriptions():
    with open("../src/data/Classes/CSCDescriptions.json", "r") as file:
        content = json.load(file)

def get_classesivetaken():
    with open("../src/data/Classes/ClassesIveTaken.json", "r") as file:
        content = json.load(file)

def get_classesivetaken():
    with open("../src/data/Classes/ClassesIveTaken.json", "r") as file:
        content = json.load(file)

def get_vscodeshortcuts():
    with open("../src/data/CompSci/VSCodeShortcuts.json", "r") as file:
        content = json.load(file)

def get_uiux_tips():
    with open("../src/data/CompSci/UIUX_Tips.json", "r") as file:
        content = json.load(file)

def get_vscodeextensions():
    with open("../src/data/CompSci/VSCodeExtensions.json", "r") as file:
        content = json.load(file)

def get_offersreceived():
    with open("../src/data/jobs/OffersReceived.json", "r") as file:
        content = json.load(file)

def get_howtogetajob():
    with open("../src/data/jobs/HowToGetAJob.json", "r") as file:
        content = json.load(file)

def get_howtogetajob():
    with open("../src/data/jobs/HowToGetAJob.json", "r") as file:
        content = json.load(file)

def get_interviewtips():
    with open("../src/data/jobs/InterviewTips.json", "r") as file:
        content = json.load(file)

def get_wheretoapply():
    with open("../src/data/jobs/WhereToApply.json", "r") as file:
        content = json.load(file)

def get_careerpathadvice():
    with open("../src/data/jobs/CareerPathAdvice.json", "r") as file:
        content = json.load(file)

def get_resumetemplatetext():
    with open("../src/data/jobs/ResumeTemplateText.json", "r") as file:
        content = json.load(file)

def get_whatislinkedin():
    with open("../src/data/LinkedIn/WhatIsLinkedIn.json", "r") as file:
        content = json.load(file)

def get_linkedintips():
    with open("../src/data/LinkedIn/LinkedInTips.json", "r") as file:
        content = json.load(file)

def get_setupprofile():
    with open("../src/data/LinkedIn/SetupProfile.json", "r") as file:
        content = json.load(file)

def get_setupjobalerts():
    with open("../src/data/LinkedIn/SetupJobAlerts.json", "r") as file:
        content = json.load(file)

def get_contacts():
    with open("../src/data/LinkedIn/Contacts.json", "r") as file:
        content = json.load(file)

def get_keyboardshortcuts():
    with open("../src/data/Other/KeyboardShortcuts.json", "r") as file:
        content = json.load(file)

def get_appstodownload():
    with open("../src/data/Other/AppsToDownload.json", "r") as file:
        content = json.load(file)

def get_terminalcommands():
    with open("../src/data/Other/TerminalCommands.json", "r") as file:
        content = json.load(file)

def get_generaltips():
    with open("../src/data/Other/GeneralTips.json", "r") as file:
        content = json.load(file)

def get_home():
    with open("../src/data/Home.json", "r") as file:
        content = json.load(file)



