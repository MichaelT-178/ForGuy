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

def make_json_object(key, value):
    """
    Converts JSON attribute to it's own object 

    Example:
    Input:
        "Title": "Visual Studio Code Shortcuts"

    Output:
        {
            "Title": "Visual Studio Code Shortcuts",
        }
    
    """
    return {key: value}

def modify_list_with_code_separation(og_list, key_to_separate):
    """
    Takes a list with JSON objects that have an attribute which is 
    an object. The JSON objects that have an attribute will be split 
    into the two different list elements. The original list element 
    without the attribute thats and object, and an object.

    Example:
    Input
        {
            "id": 2,
            "instruction": "To get started, download git. I'd recommend installing git using Homebrew. Install the Homebrew package manager using the following two commands.",
            "Code": {
                "Name": "",
                "Description": "",
                "Language": "Command",
                "FormatCode": "xcode-select --install\n\n  /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/\n  install/HEAD/install.sh)\"",
                "CopyCode": "xcode-select --install\n\n/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
            }
        },

    Output:
       {
          "id": 2,
          "instruction": "To get started, download git. I'd recommend installing git using Homebrew. Install the Homebrew package manager using the following two commands."
       }

    """

    was_found = False 

    for item in og_list:
        if key_to_separate in item:
            was_found = True
    
    if not was_found:
        return og_list
    
    modified_list = []

    for item in og_list:

        # Create a new dictionary from the original. If an object contains key_to_remove exclude it.
        item_copy = {key: value for key, value in item.items() if key != key_to_separate}
        modified_list.append(item_copy)
        
        # If key_to_remove attribute 
        if key_to_separate in item:
            modified_list.append(item[key_to_separate])

    return modified_list


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
        Results = (text + freshman_first + freshman_second + sophomore_first + 
                   sophomore_second + junior_first + junior_second + senior + ap_classes)

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

        # VSCode Shortcuts 
        title = content["VSCodeShortcuts"]["Title"]
        desc = content["VSCodeShortcuts"]["Description"]
        shortcuts = content["VSCodeShortcuts"]["Shortcuts"]

        shortcuts.append(make_json_object("Title", title))
        shortcuts.append(make_json_object("Description", desc))


        # Pycharm
        titlePy = content["PyCharm"]["Title"]
        descPy = content["PyCharm"]["Description"]
        shortcutsPy = content["PyCharm"]["Shortcuts"]

        shortcutsPy.append(make_json_object("Title", titlePy))
        shortcutsPy.append(make_json_object("Description", descPy))

        
        #Eclipse 
        titleEc = content["Eclipse"]["Title"]
        descEc = content["Eclipse"]["Description"]
        shortcutsEc = content["Eclipse"]["Shortcuts"]

        shortcutsEc.append(make_json_object("Title", titleEc))
        shortcutsEc.append(make_json_object("Description", descEc))

        #Xcode
        titleX = content["XCode"]["Title"]
        descX = content["XCode"]["Description"]
        shortcutsX = content["XCode"]["Shortcuts"]

        shortcutsX.append(make_json_object("Title", titleX))
        shortcutsX.append(make_json_object("Description", descX))

        #Slack
        titleSl = content["Slack"]["Title"]
        descSl = content["Slack"]["Description"]
        shortcutsSl = content["Slack"]["Shortcuts"]

        shortcutsSl.append(make_json_object("Title", titleSl))
        shortcutsSl.append(make_json_object("Description", descSl))


        Title = "VSCode Shortcuts"
        Link = "/compsci/VSCodeShortcuts"
        Results = shortcuts + shortcutsPy + shortcutsEc + shortcutsX + shortcutsSl

        return { "Title": Title, "Link": Link, "Results": Results }
    
def get_visualstudiocode():
    with open("../src/data/CompSci/VisualStudioCode.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        links = content["Links"]

        Title = "Visual Studio Code"
        Link = "/compsci/VisualStudioCode"
        Results = text + links

        return { "Title": Title, "Link": Link, "Results": Results }

def get_settings():
    with open("../src/data/CompSci/settings.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        settings = content["settings"]

        Title = "VSCode Settings"
        Link = "/compsci/VSCodeSettings"
        Results = text + settings

        return { "Title": Title, "Link": Link, "Results": Results }

def get_uiux_tips():
    with open("../src/data/CompSci/UIUX_Tips.json", "r") as file:
        content = json.load(file)
        
        text = content["Text"]
        tips = content["UIDesignTips"]
        ibmTips = content["IBMDesignTips"]

        ibmTips = [transform_json(tip) for tip in ibmTips]

        other = [transform_json({"Other": content["Other"]})]

        Title = "UI/UX Design Tips"
        Link = "/compsci/UIDesignTips"
        Results = text + tips + ibmTips + other

        return { "Title": Title, "Link": Link, "Results": Results }

def get_compscitips():
    with open("../src/data/CompSci/CompSciTips.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        tips = content["Tips"]
        componentData = content["ComponentData"]
        codeLinks = content["CodeLinks"]

        Title = "Comp Sci Tips"
        Link = "/compsci/CompSciTips"
        Results = text + tips + componentData + codeLinks

        return { "Title": Title, "Link": Link, "Results": Results }

def get_vscodeextensions():
    with open("../src/data/CompSci/VSCodeExtensions.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        extensions = content["Extensions"]

        Title = "VSCode Extensions"
        Link = "/compsci/VSCodeExtensions"
        Results = text + extensions

        return { "Title": Title, "Link": Link, "Results": Results }

def get_github():
    with open("../src/data/CompSci/GitHub.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        scrollLinks = content["ScrollLinks"]

        setupGithub = content["SetupGitHub"]
        setupGithub = modify_list_with_code_separation(setupGithub, "Code")

        createGitHubRepo = content["CreateGitHubRepo"]
        createGitHubRepo = modify_list_with_code_separation(createGitHubRepo, "Code")

        setupSecondGitHub = content["SetupSecondGitHub"]
        setupSecondGitHub = modify_list_with_code_separation(setupSecondGitHub, "Code")

        createSecondGitHubRepo = content["CreateSecondGitHubRepo"]
        createSecondGitHubRepo = modify_list_with_code_separation(createSecondGitHubRepo, "Code")

        amotionsWorkflowOne = content["AmotionsWorkflowOne"]
        amotionsWorkflowTwo = content["AmotionsWorkflowTwo"]

        amotionsPts = content["AmotionsPts"]
        amotionsPtsTwo = content["AmotionsPtsTwo"]
        amotionsWorkflowThree = content["AmotionsWorkflowThree"]

        threeCommands = content["ThreeCommands"]

        generalTips = content["GeneralTips"]
        generalTips = modify_list_with_code_separation(generalTips, "Code")

        gitCommands = content["GitCommands"]
        
        createFork = content["CreateFork"]
        createFork = modify_list_with_code_separation(createFork, "Code")

        resetBranch = content["ResetBranch"]
        resetBranch = modify_list_with_code_separation(resetBranch, "Code")

        existingFolderPts = content["ExistingFolderPts"]
        existingFolder = content["ExistingFolder"]

        Title = "GitHub"
        Link = "/compsci/GitHub"
        Results = (text + scrollLinks + setupGithub
                  + createGitHubRepo + setupSecondGitHub
                  + createSecondGitHubRepo + amotionsWorkflowOne
                  + amotionsWorkflowTwo + amotionsPts + amotionsPtsTwo 
                  + amotionsWorkflowThree + threeCommands + generalTips
                  + gitCommands + createFork + resetBranch
	              + existingFolderPts + existingFolder)

        return { "Title": Title, "Link": Link, "Results": Results }

# Jobs
def get_offersreceived():
    with open("../src/data/Jobs/OffersReceived.json", "r") as file:
        content = json.load(file)


        text = content["text"]
        internships = content["internships"]
        fullTime = content["fullTime"]
        interviews = content["interviews"]

        Title = "Offers I've Received"
        Link = "/Jobs/OffersReceived"
        Results = text + internships + fullTime + interviews

        return { "Title": Title, "Link": Link, "Results": Results }

def get_howtogetajob():
    with open("../src/data/Jobs/HowToGetAJob.json", "r") as file:
        content = json.load(file)

        text = content["Text"]

        tips = content["Tips"]
        tips = [transform_json(tip) for tip in tips]

        Title = "How To Get a Job"
        Link = "/Jobs/HowToGetAJob"
        Results = text + tips

        return { "Title": Title, "Link": Link, "Results": Results }

def get_interviewtips():
    with open("../src/data/Jobs/InterviewTips.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        tips = content["Tips"]

        Title = "Interview Tips"
        Link = "/jobs/InterviewTips"
        Results = text + tips

        return { "Title": Title, "Link": Link, "Results": Results }

def get_wheretoapply():
    with open("../src/data/Jobs/WhereToApply.json", "r") as file:
        content = json.load(file)

        text = content["text"]
        companies = content["Companies"]

        Title = "Where To Apply"
        Link = "/Jobs/WhereToApply"
        Results = text + companies

        return { "Title": Title, "Link": Link, "Results": Results }

def get_careerpathadvice():
    with open("../src/data/Jobs/CareerPathAdvice.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        advice = content["CareerPathAdvice"]

        Title = "Career Path Advice"
        Link = "/Jobs/CareerPathAdvice"
        Results = text + advice

        return { "Title": Title, "Link": Link, "Results": Results }

def get_resumetemplatetext():
    with open("../src/data/Jobs/ResumeTemplateText.json", "r") as file:
        content = json.load(file)

        information = content["information"]

        Title = "Resume Template"
        Link = "/Jobs/ResumeTemplate"
        Results = information

        return { "Title": Title, "Link": Link, "Results": Results }

# LinkedIn
def get_whatislinkedin():
    with open("../src/data/LinkedIn/WhatIsLinkedIn.json", "r") as file:
        content = json.load(file)
        
        info = content["Info"]

        Title = "What Is LinkedIn?"
        Link = "/LinkedIn/WhatIsLinkedIn"
        Results = info

        return { "Title": Title, "Link": Link, "Results": Results }

def get_linkedintips():
    with open("../src/data/LinkedIn/LinkedInTips.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        tips = content["LinkedInTips"]

        tips = [transform_json(tip) for tip in tips]

        Title = "LinkedIn Tips"
        Link = "/LinkedIn/LinkedinTips"
        Results = text + tips

        return { "Title": Title, "Link": Link, "Results": Results }

def get_setupprofile():
    with open("../src/data/LinkedIn/SetupProfile.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        instructions = content["Instructions"]

        Title = "Setup a Profile"
        Link = "/LinkedIn/SetupProfile"
        Results = text + instructions

        return { "Title": Title, "Link": Link, "Results": Results }

def get_setupjobalerts():
    with open("../src/data/LinkedIn/SetupJobAlerts.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        instructions = content["Instructions"]

        Title = "Setup Job Alerts"
        Link = "/LinkedIn/SetupJobAlerts"
        Results = text + instructions

        return { "Title": Title, "Link": Link, "Results": Results }

def get_contacts():
    with open("../src/data/LinkedIn/Contacts.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        contacts = content["Contacts"]

        Title = "Contacts"
        Link = "/LinkedIn/Contacts"
        Results = text + contacts

        return { "Title": Title, "Link": Link, "Results": Results }


# Other
def get_keyboardshortcuts():
    with open("../src/data/Other/KeyboardShortcuts.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        shortcuts = content["Shortcuts"]

        Title = "Keyboard Shortcuts"
        Link = "/Other/KeyboardShortcuts"
        Results = text + shortcuts

        return { "Title": Title, "Link": Link, "Results": Results }

def get_appstodownload():
    with open("../src/data/Other/AppsToDownload.json", "r") as file:
        content = json.load(file)
        
        text = content["Text"]
        apps = content["AppsToDownload"]
        kinda = content["Kinda Obviously"]


        Title = "Apps To Download"
        Link = "/Other/AppsToDownload"
        Results = text + apps + kinda

        return { "Title": Title, "Link": Link, "Results": Results }

def get_uncwpics():
    with open("../src/data/Other/UncwPics.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        pics = content["Pics"]

        Title = "UNCW Pictures"
        Link = "/Other/UncwPics"
        Results = text + pics

        return { "Title": Title, "Link": Link, "Results": Results }

def get_terminalcommands():
    with open("../src/data/Other/TerminalCommands.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        creation = content["Creation"]
        navigation = content["Navigation"]
        display = content["Display"]
        delete = content["Delete"]
        programming = content["Programming"]
        practice = content["Practice"]

        Title = "Terminal Commands"
        Link = "/Other/TerminalCommands"
        Results = text + creation + navigation + display + delete + programming + practice

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

        text = content["Text"]
        memes = content["Memes"]

        Title = "Memes"
        Link = "/Other/Memes"
        Results = text + memes

        return { "Title": Title, "Link": Link, "Results": Results }

def get_csstuffilike():
    with open("../src/data/Other/CsStuffILike.json", "r") as file:
        content = json.load(file)

        text = content["Text"]
        csStuff = content["CsStuff"]
        code = content["Code"]

        Title = "CS Stuff I Like"
        Link = "/Other/CompSciStuff"
        Results = text + csStuff + code

        return { "Title": Title, "Link": Link, "Results": Results }

def get_home():
    with open("../src/data/Home.json", "r") as file:
        content = json.load(file)

        home = content["Home"]

        Title = "Home"
        Link = "/"
        Results = home

        return { "Title": Title, "Link": Link, "Results": Results }
    
def get_contact_me():
    with open("../src/data/Contact.json", "r") as file:
        content = json.load(file)

        contact = content["Contact"]

        Title = "Contact Me"
        Link = "/ContactMe"
        Results = contact

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


# with open("delete.json", "w", encoding='utf-8') as file:
#     json.dump(all_data, file, ensure_ascii=False, indent=4)

with open("../src/data/SearchData.json", "w", encoding='utf-8') as file:
    json.dump(all_data, file, ensure_ascii=False, indent=4)
    