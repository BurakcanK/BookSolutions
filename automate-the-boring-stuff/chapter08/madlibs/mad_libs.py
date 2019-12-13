"""Mad Libs

Read in a text file and let the user add their own text anywhere the word ADJECTIVE,
NOUN, VERB or ADVERB appears in the text file. The result is printed to the screen and
saved to a new file.
"""

import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))

TEXT_FILE = os.path.join(script_dir, "text.txt")
REPLACED_FILE = os.path.join(script_dir, "replaced.txt")

with open(TEXT_FILE, "r") as infile:
    content = infile.read().strip()
    # return an iterator including all matches
    matches = re.finditer(r"ADJECTIVE|NOUN|VERB|ADVERB", content)

    for match in matches:
        if match.group() == "ADJECTIVE":
            content = re.sub(r"ADJECTIVE", input(
                "Enter an adjective: "), content, 1)
        elif match.group() == "NOUN":
            content = re.sub(r"NOUN", input("Enter a noun: "), content, 1)
        elif match.group() == "VERB":
            content = re.sub(r"VERB", input("Enter a verb: "), content, 1)
        elif match.group() == "ADVERB":
            content = re.sub(r"ADVERB", input("Enter an adverb: "), content, 1)

    print("\n" + content)

# write content to a new file
with open(REPLACED_FILE, "w") as outfile:
    outfile.write(content + "\n")
