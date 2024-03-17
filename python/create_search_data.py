import json 
import os



"""
What to do with Vue components?????????

Replace markdown.

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






# def get_thing():
#     with open("../src/data/jobs/InterviewTips.json", "r") as file:
#         content = json.load(file)