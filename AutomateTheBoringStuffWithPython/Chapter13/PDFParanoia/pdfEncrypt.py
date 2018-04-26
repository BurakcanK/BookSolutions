""" PDF Paranoia Encrypt

This script finds all of the PDF files in a directory, encrypts them using the password
provided on the command line and saves each encrypted PDF with an '_encrypted.pdf' suffix.

Usage:
    python3 pdfEncrypt.py <folder> <password>
"""

import os
import PyPDF2
import sys

# ensure usage
if len(sys.argv) != 3:
    print("Usage: python3 pdfEncrypt.py <folder> <password>")
    sys.exit()

# walk through the files
for currentFolder, _, subFiles in os.walk(sys.argv[1]):
    for subFile in subFiles:
        # find and encrypt the pdf files
        if subFile.endswith('.pdf'):
            # open a file for writing the encrypted pdf
            with open(os.path.join(currentFolder, subFile), 'rb') as inPdfFile,\
                    open(os.path.join(currentFolder, subFile[:-4] + "_encrypted.pdf"), 'wb') as outPdfFile:
                pdfReader = PyPDF2.PdfFileReader(inPdfFile)
                pdfWriter = PyPDF2.PdfFileWriter()

                # add all pages to the outfile
                for pageNum in range(pdfReader.getNumPages()):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))

                pdfWriter.encrypt(sys.argv[2])
                pdfWriter.write(outPdfFile)

            # make sure the encryption is successful before deletion
            with open(os.path.join(currentFolder, subFile[:-4] + "_encrypted.pdf"), 'rb') as encryptedFile:
                pdfReader = PyPDF2.PdfFileReader(encryptedFile)

                if pdfReader.decrypt(sys.argv[2]) == 1:
                    os.remove(os.path.join(currentFolder, subFile))
