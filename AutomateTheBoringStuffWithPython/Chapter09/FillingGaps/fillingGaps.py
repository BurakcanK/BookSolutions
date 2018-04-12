""" Filling in the Gaps

Finds all files with a given prefix in a directory, such as spam001.txt, spam002.txt,
locates any gaps in the numbering, corrects them by renaming the files after the gap.

Usage:
    python FillingGaps.py <folder> <prefix>
"""

import os, re, shutil, sys

def fillGaps(folder, prefix):
    # make sure folder is absolute
    folder = os.path.abspath(folder)

    # track folder number
    next = 1

    for fileName in sorted(os.listdir(folder)):
        # suffix after the dot
        suffix = re.search(r'\..*$', fileName)

        # check if the folder number is in order
        if fileName == prefix + "{:03}".format(next) + suffix.group():
            next += 1
        # if not rename the file according to the order
        else:
            shutil.move(os.path.join(folder, fileName),\
                        os.path.join(folder, prefix + "{:03}".format(next) + suffix.group()))
            next += 1

if len(sys.argv) != 3:
    print("Usage: python FillingGaps.py <folder> <prefix>")
    sys.exit()

fillGaps(sys.argv[1], sys.argv[2])
