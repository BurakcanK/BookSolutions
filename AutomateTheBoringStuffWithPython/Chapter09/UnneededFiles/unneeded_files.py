"""Deleting Unneeded Files

Walk through the given folder tree and search for large files.
Print these files with their absolute paths to the screen.

Usage:
    python unneeded_files.py <folder> <file_size>
"""

import os
import sys


def delete_files(folder, given_size):
    # make sure folder is absolute
    folder = os.path.abspath(folder)

    print("Files greater than >", given_size + "\n")

    # walk through the folder tree looking at sizes
    for folder_name, _, sub_files in os.walk(folder):
        for sub_file in sub_files:
            file_size = os.path.getsize(os.path.join(folder_name, sub_file))
            if file_size > int(given_size):
                print("->", os.path.join(folder_name, sub_file) + " - " + str(file_size))


# ensure usage
if len(sys.argv) != 3:
    print("Usage: python unneeded_files.py <folder> <file_size>")
    sys.exit()

delete_files(sys.argv[1], sys.argv[2])
