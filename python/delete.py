import json

with open("../src/data/Other/AppsToDownload.json", 'r') as file:
    all_data = json.load(file)


for app in all_data["AppsToDownload"]:
    print(app["Name"])
    print(app["Link"])
    print()

for app in all_data["Kinda Obviously"]:
    print(app["Name"])
    print(app["Link"])
    print()