import emoji as emoji_library
from termcolor import colored as c

# See get_all_emojis in the top-most source directory
def get_lines_containing_emojis(line):
    return [line.strip() for char in line if char in emoji_library.EMOJI_DATA]

with open("../src/data/SearchData.json", 'r') as file:

    all_emojis = []

    for line in file:

        emojis = get_lines_containing_emojis(line)

        if emojis:
            for emoji in emojis:
                all_emojis.append(emoji)
                print(emoji)

print(f"\nThis project has a total of {c(len(all_emojis), 'green')} emojis!")