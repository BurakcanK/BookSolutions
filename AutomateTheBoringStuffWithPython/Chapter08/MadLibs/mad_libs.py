#! /usr/bin/python3

"""Mad Libs

Read in a text file and let the user add their own text anywhere the word ADJECTIVE,
NOUN, VERB or ADVERB appears in the text file. The result is printed to the screen and
saved to a new file.
"""

import re

# open and read the input file
with open("story.txt", "r") as infile:
    # content of the file
    content = infile.read().strip()
    # return an iterator including all matches
    matches = re.finditer(r"ADJECTIVE|NOUN|VERB|ADVERB", content)

    # iterate over the matches
    for match in matches:
        if match.group() == "ADJECTIVE":
            content = re.sub(r"ADJECTIVE", input("Enter an adjective: "), content, 1)
        elif match.group() == "NOUN":
            content = re.sub(r"NOUN", input("Enter a noun: "), content, 1)
        elif match.group() == "VERB":
            content = re.sub(r"VERB", input("Enter a verb: "), content, 1)
        elif match.group() == "ADVERB":
            content = re.sub(r"ADVERB", input("Enter an adverb: "), content, 1)
    # print the result to the screen
    print("\n" + content)

# write content to a new file
with open("replaced.txt", "w") as outfile:
    outfile.write(content + "\n")
