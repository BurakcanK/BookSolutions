"""Regex Search

Open all .txt files in a folder and searches for any line that matches a
user-supplied regular expression. Results are printed to the screen.

Usage:
    python3 regex_search.py <folder> "<regex>"
"""

import os
import re
import sys

FOLDER_PATH = os.path.abspath(sys.argv[1])

if len(sys.argv) != 3:
    print('Usage: python3 regex_search.py <folder> "<regex>"')
    sys.exit()

for text_folder in os.listdir(FOLDER_PATH):
    with open(os.path.join(FOLDER_PATH, text_folder), "r") as text_file:
        lines = text_file.readlines()
        for line in lines:
            if re.search(r"{}".format(sys.argv[2]), line):
                print(text_folder, "-> " + line.strip())
