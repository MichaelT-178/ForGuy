import subprocess
from termcolor import colored as c

def write_to_clipboard(output: str):
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

num_of_instructions = int(input("Enter num of instructions: "))
include_block = input("Code block? (y/n): ")

string = ""

for i in range(num_of_instructions):
    block = include_block.lower().strip() in ["yes", "y"]

    string += "\t\t\t\t{\n"
    string += f"\t\t\t\t\t\"id\": {i + 1},\n"
    string += f'\t\t\t\t\t"instruction": ""{"," if block else ""}\n'

    if block:
        string += "\t\t\t\t\t\"Code\": {\n"
        string += "\t\t\t\t\t\t\"Name\": \"\",\n"
        string += "\t\t\t\t\t\t\"Description\": \"\",\n"
        string += "\t\t\t\t\t\t\"Language\": \"\",\n"
        string += "\t\t\t\t\t\t\"FormatCode\": \"\",\n"
        string += "\t\t\t\t\t\t\"CopyCode\": \"\"\n"
        string += "\t\t\t\t\t}\n"

    string += "\t\t\t\t},\n"
    
print(string.strip())
write_to_clipboard(string.strip())

print(c("Successfully Copied to clipboard!".upper(), "green"))