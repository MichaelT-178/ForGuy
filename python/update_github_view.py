import json
import re 

text_dict = {}

with open("../src/data/CompSci/GitHub.json", "r") as file:
    content = json.load(file)
    texts = content["Text"]

    for index, text in enumerate(texts):
        text_dict[text["text-id"]] = index


all_lines = []
with open("../src/Views/CompSci/Github.vue", 'r') as file:
    for line in file:

        real_line = line 

        for key, value in text_dict.items():
            if key in line:
                pattern = r'text\[(?:[1-9]?[0-9]|100)\]'
                real_line = re.sub(pattern, f"text[{value}]", line)

        all_lines.append(real_line)

            # for key, value in text_dict.items():
with open("../src/Views/CompSci/Github.vue", 'w') as file:
    for line in all_lines:
        file.write(line)