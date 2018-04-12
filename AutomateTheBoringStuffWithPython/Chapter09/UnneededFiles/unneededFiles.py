#! /usr/bin/python3

""" Deleting Unneeded Files

This script walks through the given folder tree and searches for large files.
Prints these files with their absolute paths to the screen.

Usage:
    python UnneededFiles.py <folder> <fileSize>
"""

import os, sys

def deleteFiles(folder, fileSize):
    # make sure folder is absolute
    folder = os.path.abspath(folder)

    print("\nFiles greater than >", fileSize + "\n")

    # walk through the folder tree looking at sizes
    for folderName, _, subFiles in os.walk(folder):
        # look for subfiles
        for subFile in subFiles:
            if os.path.getsize(os.path.join(folderName, subFile)) > int(fileSize):
                print("-> ", os.path.join(folderName, subFile) + " -> "\
                           + str(os.path.getsize(os.path.join(folderName, subFile))) + "\n")

# ensure usage
if len(sys.argv) != 3:
    print("Usage: python UnneededFiles.py <folder> <fileSize>")
    sys.exit()

deleteFiles(sys.argv[1], sys.argv[2])
