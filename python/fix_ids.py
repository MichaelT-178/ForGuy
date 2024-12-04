import json
from termcolor import colored as c

# List of file paths with associated types
# 1 -> Regular JSON file
# 2 -> One set instructions
# 3 -> MultiSet Instructions
# 4 -> DisplayLinks
file_paths = [
    # Type 1
    {"path": "../src/data/SearchPages.json", "type": 1},

    # Type 2
    {"path": "SwiftData.json",   "type": 2},
    {"path": "NodeServer.json",  "type": 2},
    {"path": "PyiCloud.json",    "type": 2},
    {"path": "FlaskSQLite.json", "type": 2},
    {"path": "Youtube.json",     "type": 2},

    # Type 3 
    {"path": "SpringApp.json",    "type": 3},
    {"path": "RedditBotAWS.json", "type": 3},
    {"path": "EmailJS.json",      "type": 3},
    {"path": "FlaskPost.json",    "type": 3},
    {"path": "Django.json",       "type": 3},
    {"path": "DeployDjango.json", "type": 3},
    {"path": "DeployPost.json",   "type": 3},

    # Type 4
    {"path": "DisplayLinks.json", "type": 4},
]

# Function to display file paths grouped by type
def display_file_paths_by_type():
    print(c("\nFile Paths:\n", "cyan"))
    file_types = {1: "Type 1", 2: "Type 2", 3: "Type 3", 4: "Type 4"}

    grouped_files = {key: [] for key in file_types.keys()}

    for i, file in enumerate(file_paths):
        grouped_files[file["type"]].append(f"{i + 1}. {file['path']}")

    # Print files by type
    for file_type, files in grouped_files.items():
        if files:
            print(c(f"{file_types[file_type]}", "yellow"))
            print("\n".join([c(file, "cyan") for file in files]))
            print()


def get_file_choice():
    display_file_paths_by_type()

    while True:
        try:
            choice = int(input(c(f"Enter the file number to use (1-{len(file_paths)}): ", 'magenta')))

            if 1 <= choice <= len(file_paths):
                return file_paths[choice - 1]
            else:
                print(c("Please enter a valid number corresponding to a file.", "red"))

        except ValueError:
            print(c("Invalid input. Please enter a number.", "red"))



selected_file = get_file_choice()
file_path = selected_file["path"]
file_type = selected_file["type"]

with open(file_path, 'r') as file:
    if file_type == 1:
        data = json.load(file)

        # For normal files
        for i, item in enumerate(data):
            item["id"] = i + 1
    elif file_type == 2:
        complete_path = "../src/data/CompSci/Instructions"
        with open(f"{complete_path}/{file_path}", 'r') as nested_file:
            data = json.load(nested_file)

        # For One set Instructions 
        data_set = data["Instructions"]
        for i, item in enumerate(data_set):
            item["id"] = i + 1
    elif file_type == 3:
        complete_path = "../src/data/CompSci/Instructions"
        with open(f"{complete_path}/{file_path}", 'r') as nested_file:
            data = json.load(nested_file)

        # For MultiSet Instructions
        for data_sets in data["MultiSet"]:
            current_set = data_sets["Instructions"]
            for i, item in enumerate(current_set):
                item["id"] = i + 1
    elif file_type == 4:
        complete_path = "../src/data/CompSci/Instructions"
        with open(f"{complete_path}/{file_path}", 'r') as nested_file:
            data = json.load(nested_file)

        # For DisplayLinks
        for i, item in enumerate(data['DisplayLinks']['FrameworkProjects']['links']):
            print(item)
            item["id"] = i + 1


with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    print(c("Updated Successfully!", "green"))
