"""ExtendedMCB - Save and load pieces of text to the clipboard.

                      save <keyword> - Save clipboard to keyword.
                      delete <keyword> - Delete the keyword.
Usage:  python mcb.py <keyword> - Load keyword to clipboard.
                      list - Load all keywords to clipboard.
                      delete - Delete all of the entries in DB.
"""

import pyperclip
import shelve
import sys

# open the database
mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
    # save clipboard content
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    # delete clipboard content
    elif sys.argv[1].lower() == 'delete':
        del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    # clear all database
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
    # fetch content from DB to clipboard
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

# close the DB
mcb_shelf.close()
