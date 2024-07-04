import json 


# file_path = "../src/data/SearchPages.json"
# file_path = "../src/data/CompSci/Instructions/SwiftData.json"
file_path = "../src/data/CompSci/Instructions/RedditBotAWS.json"
# file_path = "../src/data/CompSci/Instructions/SpringApp.json"
# file_path = "../src/data/CompSci/Instructions/NodeServer.json"

with open(file_path, 'r') as file:
    data = json.load(file)
    
    # for i, item in enumerate(data):
    #     item["id"] = i + 1


    # data_set = data["Instructions"]
    
    # for i, item in enumerate(data_set):
    #     item["id"] = i + 1
    
    
    data_set = data["MultiSet"][5]["Instructions"]

    for i, item in enumerate(data_set):
        item["id"] = i + 1




with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    print("Updated Successfully!")
