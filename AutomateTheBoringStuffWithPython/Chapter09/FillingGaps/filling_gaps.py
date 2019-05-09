"""Filling in the Gaps

Find all files with a given prefix in a directory, such as spam001.txt, spam002.txt,
locate any gaps in the numbering, correct them by renaming the files after the gap.

Usage:
    python filling_gaps.py <folder> <prefix>
"""

import os
import shutil
import sys


def fill_gaps(folder, prefix):
    # make sure folder is absolute
    folder = os.path.abspath(folder)

    # track folder number
    num = 1

    for file_name in sorted(os.listdir(folder)):
        suffix = file_name.split(".")[1]

        # check if the folder number is in order
        if file_name == prefix + "{:03}".format(num) + suffix:
            num += 1
        # if not rename the file according to the order
        else:
            shutil.move(os.path.join(folder, file_name),
                        os.path.join(folder, prefix + "{:03}.".format(num) + suffix))
            num += 1


if len(sys.argv) != 3:
    print("Usage: python filling_gaps.py <folder> <prefix>")
    sys.exit()

fill_gaps(sys.argv[1], sys.argv[2])
