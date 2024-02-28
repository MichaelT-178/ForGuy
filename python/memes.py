#/Users/michaeltotaro/top-bar/src/assets/memes

import os

def list_files(directory):

    all_memes = []

    for entry in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, entry)):
            all_memes.append(entry)

    return all_memes


directory_path = '../../top-bar/src/assets/memes'
all_memes = list_files(directory_path)


for idx, meme in enumerate(all_memes):
    # print(f'import Meme{idx + 1} from "../assets/memes/{meme}";')

    print('    { text: "t", image: Meme',end="")
    print(idx + 1, end="")
    print(' },', end="")
    print(f' //{meme}')