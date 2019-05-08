"""Regex Search

Open all .txt files in a folder and searches for any line that matches a
user-supplied regular expression. Results are printed to the screen.

Usage:
    python3 regex_search.py <folder> "<regex>"
"""

import os
import re
import sys

# ensure usage
if len(sys.argv) != 3:
    print('Usage: python3 regex_search.py <folder> "<regex>"')
    sys.exit()

# location of the txt files
loc = os.path.abspath(sys.argv[1])

# iterate over the files in the location
for infile in os.listdir(loc):
    # open each file, joined with absolute path
    with open(os.path.join(loc, infile), "r") as text_file:
        # read the file lines to a list
        lines = text_file.readlines()

        for line in lines:
            if re.search(r"{}".format(sys.argv[2]), line):
                print("-> " + line.strip())
