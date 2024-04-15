with open("yeet.txt", "r") as file:
    print('{')
    print('    "settings": [')
    for line in file:

        if line.strip() != "":
            cool = line.strip().replace('"', '\\"')
            print('        {')
            print(f'            "text": "{cool}"')
            print('        },')
    print('    ]')
    print('}')