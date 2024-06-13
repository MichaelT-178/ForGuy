import json 


# file_path = "../src/data/SearchPages.json"
# file_path = "../src/data/CompSci/Instructions/SetupAngular.json"
file_path = "../src/data/CompSci/Instructions/SpringApp.json"

with open(file_path, 'r') as file:
    data = json.load(file)

    data_set = data["MultiSet"][1]["Instructions"]

    for i, item in enumerate(data_set):
        item["id"] = i + 1

    # for i, item in enumerate(data):
    #     item["id"] = i + 1


with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    print("Updated Successfully!")
