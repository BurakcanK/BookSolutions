#! /usr/bin/python3

""" ExtendedMCB - Saves and loads pieces of text to the clipboard.

                             save <keyword> - Saves clipboard to keyword.
                             delete <keyword> - Deletes the keyword.
Usage:  python ./ExtendedMCB <keyword> - Loads keyword to clipboard.
                             list - Loads all keywords to clipboard.
                             delete - Deletes all of the entries in DB.
"""

import pyperclip, shelve, sys

# open the database
mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    # save clipboard content
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # delete clipboard content
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # clear all database
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    # fetch content from DB to clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

# close the DB
mcbShelf.close()
