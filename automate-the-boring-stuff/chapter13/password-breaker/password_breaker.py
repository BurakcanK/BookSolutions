"""Brute-Force PDF Password Breaker

Try every possible english word on an encrypted PDF until the
one that's working.
"""

import os
import PyPDF2
import sys

DICT = os.path.join(
    os.path.dirname(__file__),
    "dictionary.txt"
)

# ensure usage
if len(sys.argv) != 2:
    print("Usage: python3 password_breaker.py <pdf_file>")
    sys.exit()

with open(DICT, "r") as dictionary, open(sys.argv[1], "rb") as pdf_file:
    print("Decryption started...")
    for word in dictionary:
        word = word.strip()
        pdr_reader = PyPDF2.PdfFileReader(pdf_file)

        # try to decrypt pdf with every possible word
        if pdr_reader.decrypt(word.lower()) == 1:
            print("Password is found :", word.lower())
            break
        elif pdr_reader.decrypt(word) == 1:
            print("Password is found :", word)
            break
        else:
            continue
    else:
        print("Unsuccessful..")
