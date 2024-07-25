import re

with open("../src/components/Memes.vue", "r") as file:

    pattern = r'.*Meme\d{1,2}.*'

    count = 1
    import_statements = True

    all_lines = []
    
    for line in file:

        if "image: " in line and import_statements:
            count = 1
            import_statements = False

        if re.search(pattern, line):
            new_line = re.sub(r'Meme\d{1,2}', f'Meme{count}', line)[:-1]
            count += 1
            all_lines.append(new_line)
        else:
            all_lines.append(line[:-1])

with open("../src/components/Memes.vue", "w", encoding='utf-8') as f:
    for line in all_lines:
        print(line)
        f.write(line + '\n') 
