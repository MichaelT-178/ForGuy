import os

directory_path = '../src/data/CompSci/Instructions/'

files_and_directories = os.listdir(directory_path)

file_names = [f for f in files_and_directories if os.path.isfile(os.path.join(directory_path, f))]

print(file_names)
