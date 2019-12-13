"""ExtendedMCB - Save and load pieces of text to the clipboard.

                      save <keyword> - Save clipboard to keyword.
                      delete <keyword> - Delete the keyword.
Usage:  python mcb.py <keyword> - Load keyword to clipboard.
                      list - Load all keywords to clipboard.
                      delete - Delete all of the entries in DB.
"""

import os
import pyperclip
import shelve
import sys

# open the database
mcb_shelf = shelve.open(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "mcb"
))

if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "delete":
        del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == "delete":
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
