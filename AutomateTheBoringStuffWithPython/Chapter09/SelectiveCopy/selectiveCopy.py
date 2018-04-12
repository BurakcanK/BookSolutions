""" Selective Copy

Walks through a folder tree and searches for files with a certain file
extension (such as .jpg or .pdf), copies these files into a new folder.

Usage :     python3 SelectiveCopy.py <src> <dest> <.extension>

Example :   python3 SelectiveCopy.py Delicious/ CopiedFiles .txt
"""

import os, shutil, sys

def main(argv):
    if len(argv) != 4:
        print("Usage: python SelectiveCopy.py <src> <dest> <.extension>")
        sys.exit()
    selectiveCopy(argv[1], argv[2], argv[3])

def selectiveCopy(src, dest, extension):
    # create a folder to copy files into
    try:
        os.makedirs(dest)
    except FileExistsError:
        print("Destination file exists:", dest)
        sys.exit()

    # walk through the source folder looking for extension
    for folderName, _, subFiles in os.walk(src):
        print("Searching within", folderName)

        for subFile in subFiles:
            if subFile.endswith(extension):
                loc = shutil.copy(os.path.join(folderName, subFile), dest)
                print("Copied to -> ", loc)

if __name__ == "__main__":
    main(sys.argv)
