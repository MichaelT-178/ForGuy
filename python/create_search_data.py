import json 
import os
import subprocess
from termcolor import colored as c

"""
What to do with Vue components?????????

Replace markdown.

ADD PATH AND NAME TO JSON FILES 

"""

def get_files_in_directory(path):
    files = os.listdir(path)
    return files

def write_to_clipboard(output: str):
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))
    
paths = [
    '../src/data/Classes/',
    '../src/data/CompSci/',
    '../src/data/jobs/',
    '../src/data/LinkedIn/',
    '../src/data/Other/',
]

all_functions_str = ""

for path in paths:

    all_functions_str += f"\n# {path.replace('../src/data/', '')[:-1]}\n"

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

func_vars = []

for path in paths:

    for file_name in get_files_in_directory(path):
        file = file_name.replace(".json", "")
        
        if ".docx" not in file_name and ".vue" not in file_name:
            func_call_str = f'{file.lower()} = get_{file.lower()}()\n'
            func_vars.append(file.lower())

        all_functions_str += func_call_str

all_functions_str = all_functions_str

all_functions_str += f"\nall_data = {func_vars}\n"

print(all_functions_str)
write_to_clipboard(all_functions_str)
print(c("Copied to clipboard!", "green"))





