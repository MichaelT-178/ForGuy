import json 


with open("../src/data/Classes/ClassesIveTaken.json", "r") as file:
    content = json.load(file)

freshman_classes = content["Freshman"]["First"]
freshman_classes_two = content["Freshman"]["Second"]
sophomore_classes = content["Sophomore"]["First"]
sophomore_classes_two = content["Sophomore"]["Second"]
junior_classes = content["Junior"]["First"]
junior_classes_two = content["Junior"]["Second"]
senior = content["Senior"]

for a_class in freshman_classes:
    print(a_class["Name"])
for a_class in freshman_classes_two:
    print(a_class["Name"])
for a_class in sophomore_classes:
    print(a_class["Name"])
for a_class in sophomore_classes_two:
    print(a_class["Name"])
for a_class in junior_classes :
    print(a_class["Name"])
for a_class in junior_classes_two:
    print(a_class["Name"])
for a_class in senior:
    print(a_class["Name"])