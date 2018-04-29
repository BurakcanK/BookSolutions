""" Brute-Force PDF Password Breaker

Tries every possible english word on an encrypted PDF until it finds the
one that's working.
"""

import PyPDF2
import sys

# ensure usage
if len(sys.argv) != 2:
    print("Usage: python3 passwordBreaker.py <pdfFile>")
    sys.exit()

# open the dictionary and the pdf file
with open("dictionary.txt", "r") as dictionary, open(sys.argv[1], "rb") as pdfFile:

    print("Decryption started...")
    for word in dictionary:
        word = word.strip()
        pdfReader = PyPDF2.PdfFileReader(pdfFile)

        # try to decrypt pdf with every possible word
        if pdfReader.decrypt(word.lower()) == 1:
            print("Password is found :", word.lower())
            break
        elif pdfReader.decrypt(word) == 1:
            print("Password is found :", word)
            break
        else:
            continue
    else:
        print("Unsuccessful..")
