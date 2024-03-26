import json 

with open("../src/data/Classes/ClassesIveTaken.json", "r") as file:
    content = json.load(file)

freshman_classes = content["Freshman"]["First"]
freshman_classes_two = content["Freshman"]["Second"]
sophomore_classes = content["Sophomore"]["First"]
sophomore_classes_two = content["Sophomore"]["Second"]
junior_classes = content["Junior"]["First"]
junior_classes_two = content["Junior"]["Second"]
senior = content["Senior"]["First"]


def print_json(json_data):
    formatted_json = json.dumps(json_data, indent=4)
    return formatted_json + ","




for a_class in freshman_classes:
    if "CSC" in a_class["Name"].upper():
        print(print_json(a_class))
for a_class in freshman_classes_two:
    if "CSC" in a_class["Name"].upper():
        print(print_json(a_class))
for a_class in sophomore_classes:
    if "CSC" in a_class["Name"].upper():
        print(print_json(a_class))
for a_class in sophomore_classes_two:
    if "CSC" in a_class["Name"].upper():
        print(print_json(a_class))
for a_class in junior_classes :
    if "CSC" in a_class["Name"].upper():
        print(print_json(a_class))
for a_class in junior_classes_two:
    if "CSC" in a_class["Name"].upper():
        print(print_json(a_class))
for a_class in senior:
    if "CSC" in a_class["Name"].upper():
        print(print_json(a_class))
