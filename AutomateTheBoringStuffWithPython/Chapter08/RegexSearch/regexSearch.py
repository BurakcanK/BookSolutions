#! /usr/bin/python3

""" Regex Search

Opens all .txt files in a folder and searches for any line that matches a
user-supplied regular expression. Results are printed to the screen.

Usage:
    python3 RegexSearch.py <folder> "<regex>"
"""

import os, re, sys

# ensure usage
if len(sys.argv) != 3:
    print('Usage: python3 RegexSearch.py <folder> "<regex>"')
    sys.exit()

# location of the txt files
loc = os.path.abspath(sys.argv[1])

# iterate over the files in the location
for inFile in os.listdir(loc):
    # open each file, joined with absolute path
    with open(os.path.join(loc, inFile), 'r') as textFile:
        # read the file lines to a list
        lines = textFile.readlines()

        for line in lines:
            if re.search(r'{}'.format(sys.argv[2]), line):
                print("-> " + line.strip())
