import json 
import os
import subprocess
from termcolor import colored as c

"""
What to do with Vue components?????????

Replace markdown.

ADD PATH AND NAME TO JSON FILES 

"""


def format_json(data):
    return json.dumps(data, indent=4)

def transform_json(json_obj):
    """
    Converts any attributes in a json object that are lists into a comma-separated string.
    Keeps the original key for each attribute. If none of the attributes are lists, returns 
    the unmodified json object.

    Example:
    Input:
        "Classes": [
            "CSC 360",
            "CSC 380"
        ],
    
    Output:
        "Classes": "CSC 360, CSC 380"
    """

    result = {}
    
    for key, value in json_obj.items():
        if isinstance(value, list):
            result[key] = ', '.join(value)
        else:
            result[key] = value
    
    return result


# Classes
def get_classestoavoid():
    with open("../src/data/Classes/ClassesToAvoid.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        classes = content["Classes"]
        professors = content["Professors"]


        Title = "Classes To Avoid"
        Link = "/Classes/ClassesToAvoid"
        Results = text + classes + professors

        return { "Title": Title, "Link": Link, "Results": Results }


def get_classrecommendations():
    with open("../src/data/Classes/ClassRecommendations.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        classes = content["Classes"]
        professors = content["Professors"]

        professors = [transform_json(obj) for obj in professors]

        Title = "Class Recommendations"
        Link = "/Classes/ClassRecommendations"
        Results = text + classes + professors

        return { "Title": Title, "Link": Link, "Results": Results }



def get_usefulcertifications():
    with open("../src/data/Classes/UsefulCertifications.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        cloud_certs = content["Cloud Certifications"]
        essential_skills = content["Certifications for Essential Skills"]
        machine_learning = content["Machine Learning Certifications"]
        degrees = content["Academic Certifications and Degrees"]
        tips = content["GeneralTips"]


        Title = "Useful Certifications"
        Link = "/Classes/Certifications"
        Results = text + cloud_certs + essential_skills + machine_learning + degrees + tips

        return { "Title": Title, "Link": Link, "Results": Results }

def get_cscdescriptions():
    with open("../src/data/Classes/CSCDescriptions.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        courses = content["Courses"]

        courses = [transform_json(course) for course in courses]

        Title = "CSC Descriptions"
        Link = "/Classes/CSCDescriptions"
        Results = text + courses

        return { "Title": Title, "Link": Link, "Results": Results }

def get_classesivetaken():
    with open("../src/data/Classes/ClassesIveTaken.json", "r") as file:
        content = json.load(file)

        text = content["Text"]

        freshman_first = content["Freshman"]["First"]
        freshman_second = content["Freshman"]["Second"]

        sophomore_first = content["Sophomore"]["First"]
        sophomore_second = content["Sophomore"]["Second"]

        junior_first = content["Junior"]["First"]
        junior_second = content["Junior"]["Second"]

        senior = content["Senior"]["First"]

        ap_classes = content["Ap Classes"]

        sophomore_first = [transform_json(course) for course in sophomore_first]
        sophomore_second = [transform_json(course) for course in sophomore_second]
        junior_first = [transform_json(course) for course in junior_first]
        junior_second = [transform_json(course) for course in junior_second]
        senior = [transform_json(course) for course in senior]


        Title = "Classes I've Taken"
        Link = "/Classes/ClassesIveTaken"
        Results = text + freshman_first + freshman_second + sophomore_first + sophomore_second + junior_first + junior_second + senior + ap_classes

        return { "Title": Title, "Link": Link, "Results": Results }

def get_compsciminor():
    with open("../src/data/Classes/CompSciMinor.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        classes = content["Classes"]
        semester_classes = content["SemesterClasses"]
        
        classes = [transform_json(course) for course in classes]
        semester_classes = [transform_json(course) for course in semester_classes]
        

        Title = "Comp Sci Minor"    
        Link = "/Classes/CompSciMinor"
        Results = text + classes + semester_classes

        return { "Title": Title, "Link": Link, "Results": Results }


# CompSci

def get_vscodeshortcuts():
    with open("../src/data/CompSci/VSCodeShortcuts.json", "r") as file:
        content = json.load(file)

        Title = "VSCode Shortcuts"
        Link = "/compsci/VSCodeShortcuts"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }
    
def get_visualstudiocode():
    with open("../src/data/CompSci/VisualStudioCode.json", "r") as file:
        content = json.load(file)

        Title = "Visual Studio Code"
        Link = "/compsci/VisualStudioCode"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_settings():
    with open("../src/data/CompSci/settings.json", "r") as file:
        content = json.load(file)

        Title = "VSCode Settings"
        Link = "/compsci/VSCodeSettings"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_uiux_tips():
    with open("../src/data/CompSci/UIUX_Tips.json", "r") as file:
        content = json.load(file)

        Title = "UI/UX Design Tips"
        Link = "/compsci/UIDesignTips"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_compscitips():
    with open("../src/data/CompSci/CompSciTips.json", "r") as file:
        content = json.load(file)

        Title = "Comp Sci Tips"
        Link = "/compsci/CompSciTips"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_vscodeextensions():
    with open("../src/data/CompSci/VSCodeExtensions.json", "r") as file:
        content = json.load(file)

        Title = "VSCode Extensions"
        Link = "/compsci/VSCodeExtensions"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_github():
    with open("../src/data/CompSci/GitHub.json", "r") as file:
        content = json.load(file)

        Title = "GitHub"
        Link = "/compsci/GitHub"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }


# Jobs
def get_offersreceived():
    with open("../src/data/Jobs/OffersReceived.json", "r") as file:
        content = json.load(file)

        Title = "Offers I've Received"
        Link = "/Jobs/OffersReceived"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_howtogetajob():
    with open("../src/data/Jobs/HowToGetAJob.json", "r") as file:
        content = json.load(file)

        Title = ""
        Link = ""
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_howtogetajob():
    with open("../src/data/Jobs/HowToGetAJob.json", "r") as file:
        content = json.load(file)

        Title = "How To Get a Job"
        Link = "/Jobs/HowToGetAJob"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_interviewtips():
    with open("../src/data/Jobs/InterviewTips.json", "r") as file:
        content = json.load(file)

        Title = "Interview Tips"
        Link = "/jobs/InterviewTips"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_wheretoapply():
    with open("../src/data/Jobs/WhereToApply.json", "r") as file:
        content = json.load(file)

        Title = "Where To Apply"
        Link = "/Jobs/WhereToApply"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_careerpathadvice():
    with open("../src/data/Jobs/CareerPathAdvice.json", "r") as file:
        content = json.load(file)

        Title = "Career Path Advice"
        Link = "/Jobs/CareerPathAdvice"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_resumetemplatetext():
    with open("../src/data/Jobs/ResumeTemplateText.json", "r") as file:
        content = json.load(file)

        Title = "Resume Template"
        Link = "/Jobs/ResumeTemplate"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }


# LinkedIn
def get_whatislinkedin():
    with open("../src/data/LinkedIn/WhatIsLinkedIn.json", "r") as file:
        content = json.load(file)

        Title = "What Is LinkedIn?"
        Link = "/LinkedIn/WhatIsLinkedIn"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_linkedintips():
    with open("../src/data/LinkedIn/LinkedInTips.json", "r") as file:
        content = json.load(file)

        Title = "LinkedIn Tips"
        Link = "/LinkedIn/LinkedinTips"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_setupprofile():
    with open("../src/data/LinkedIn/SetupProfile.json", "r") as file:
        content = json.load(file)

        Title = "Setup a Profile"
        Link = "/LinkedIn/SetupProfile"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_setupjobalerts():
    with open("../src/data/LinkedIn/SetupJobAlerts.json", "r") as file:
        content = json.load(file)

        Title = "Setup Job Alerts"
        Link = "/LinkedIn/SetupJobAlerts"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_contacts():
    with open("../src/data/LinkedIn/Contacts.json", "r") as file:
        content = json.load(file)

        Title = "Contacts"
        Link = "/LinkedIn/Contacts"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }


# Other
def get_keyboardshortcuts():
    with open("../src/data/Other/KeyboardShortcuts.json", "r") as file:
        content = json.load(file)

        Title = "Keyboard Shortcuts"
        Link = "/Other/KeyboardShortcuts"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_appstodownload():
    with open("../src/data/Other/AppsToDownload.json", "r") as file:
        content = json.load(file)

        Title = "Apps To Download"
        Link = "/Other/AppsToDownload"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_uncwpics():
    with open("../src/data/Other/UncwPics.json", "r") as file:
        content = json.load(file)

        Title = "UNCW Pictures"
        Link = "/Other/UncwPics"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_terminalcommands():
    with open("../src/data/Other/TerminalCommands.json", "r") as file:
        content = json.load(file)

        Title = "Terminal Commands"
        Link = "/Other/TerminalCommands"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_generaltips():
    with open("../src/data/Other/GeneralTips.json", "r") as file:
        content = json.load(file)

        Title = "General Tips"
        Link = "/Other/GeneralTips"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_memes():
    with open("../src/data/Other/Memes.json", "r") as file:
        content = json.load(file)

        Title = "Memes"
        Link = "/Other/Memes"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_csstuffilike():
    with open("../src/data/Other/CsStuffILike.json", "r") as file:
        content = json.load(file)

        Title = "CS Stuff I Like"
        Link = "/Other/CompSciStuff"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }

def get_home():
    with open("../src/data/Home.json", "r") as file:
        content = json.load(file)

        Title = "Home"
        Link = "/"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }
    
def get_contact_me():
    with open("../src/data/Contact.json", "r") as file:
        content = json.load(file)

        Title = "Contact Me"
        Link = "/ContactMe"
        Results = None

        return { "Title": Title, "Link": Link, "Results": Results }



classestoavoid = get_classestoavoid()
classrecommendations = get_classrecommendations()
usefulcertifications = get_usefulcertifications()
cscdescriptions = get_cscdescriptions()
classesivetaken = get_classesivetaken()
compsciminor = get_compsciminor()
compsciminor = get_compsciminor()
vscodeshortcuts = get_vscodeshortcuts()
visualstudiocode = get_visualstudiocode()
settings = get_settings()
uiux_tips = get_uiux_tips()
compscitips = get_compscitips()
vscodeextensions = get_vscodeextensions()
github = get_github()
offersreceived = get_offersreceived()
howtogetajob = get_howtogetajob()
howtogetajob = get_howtogetajob()
interviewtips = get_interviewtips()
wheretoapply = get_wheretoapply()
careerpathadvice = get_careerpathadvice()
resumetemplatetext = get_resumetemplatetext()
whatislinkedin = get_whatislinkedin()
linkedintips = get_linkedintips()
setupprofile = get_setupprofile()
setupjobalerts = get_setupjobalerts()
contacts = get_contacts()
keyboardshortcuts = get_keyboardshortcuts()
appstodownload = get_appstodownload()
uncwpics = get_uncwpics()
terminalcommands = get_terminalcommands()
generaltips = get_generaltips()
memes = get_memes()
csstuffilike = get_csstuffilike()
home = get_home()
contactme = get_contact_me()


all_data = [
    home, 

    wheretoapply,
    resumetemplatetext,
    howtogetajob,
    offersreceived,
    interviewtips,
    careerpathadvice,

    whatislinkedin,
    setupprofile,
    setupjobalerts,
    linkedintips,
    contacts,

    classrecommendations,
    classesivetaken,
    cscdescriptions,
    classestoavoid,
    compsciminor,
    usefulcertifications,

    visualstudiocode,
    github,
    settings,
    uiux_tips,
    vscodeextensions,
    vscodeshortcuts,
    compscitips,

    generaltips,
    appstodownload,
    csstuffilike,
    terminalcommands,
    keyboardshortcuts,
    memes,
    uncwpics,

    contactme
]



print(format_json(classesivetaken))