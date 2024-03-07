import json 

with open("../src/data/CompSci/VSCodeExtensions.json", "r") as file:
    file_content = json.load(file)


extensions = file_content["Extensions"]

for extension in extensions:
    print(f"`{extension['Name']}%0A` +")
    print(f"`{extension['Link']}%0A%0A` +")
    print()