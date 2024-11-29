from os import path
from os import listdir
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

files = listdir(current_dir)
print(files)

for file in files:
    if not file.endswith(".html"):
        files.remove(file)

print(files)