"""Selective Copy

Walk through a folder tree and search for files with a certain file
extension (such as .jpg or .pdf), copy these files into a new folder.

Usage :     python3 selective_copy.py <src> <dest> <.extension>

Example :   python3 selective_copy.py Delicious/ CopiedFiles .txt
"""

import os
import shutil
import sys


def main(argv):
    if len(argv) != 3:
        print("Usage: python selective_copy.py <src> <dest> <.extension>")
        sys.exit()

    src = os.path.abspath(argv[0])
    dest = os.path.abspath(argv[1])
    ext = argv[2]

    selective_copy(src, dest, ext)


def selective_copy(src, dest, extension):
    # create a folder to copy files into
    try:
        os.makedirs(dest)
    except FileExistsError:
        print("Destination file exists:", dest)
        sys.exit()

    # walk through the source folder looking for extension
    for folder_name, _, sub_files in os.walk(src):
        print("Searching within", folder_name)

        for sub_file in sub_files:
            if sub_file.endswith(extension):
                loc = shutil.copy(os.path.join(folder_name, sub_file), dest)
                print("Copied to -> ", loc)


if __name__ == "__main__":
    main(sys.argv[1:])
