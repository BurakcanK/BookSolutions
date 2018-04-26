""" PDF Paranoia Decrypt

This script finds all of the PDF files in a directory, decrypts them using the password
provided on the command line and saves each decrypted PDF with an '_decrypted.pdf' suffix.
If decryption fails, informs the user and proceeds to the next pdf file.

Usage:
    python3 pdfDecrypt.py <folder> <password>
"""

import os
import PyPDF2
import sys

# ensure usage
if len(sys.argv) != 3:
    print("Usage: python3 pdfDecrypt.py <folder> <password>")
    sys.exit()

# walk through the files
for currentFolder, _, subFiles in os.walk(sys.argv[1]):
    for subFile in subFiles:
        # find and decrypt the pdf files
        if subFile.endswith('.pdf'):
            # try to decrypt the encrypted file
            with open(os.path.join(currentFolder, subFile), 'rb') as inPdfFile:
                pdfReader = PyPDF2.PdfFileReader(inPdfFile)

                # decryption successful
                if pdfReader.decrypt(sys.argv[2]) == 1:
                    with open(os.path.join(currentFolder, subFile[:-4] + "_decrypted.pdf"), 'wb') as outPdfFile:
                        pdfWriter = PyPDF2.PdfFileWriter()

                        # add all pages to the outfile
                        for pageNum in range(pdfReader.getNumPages()):
                            pdfWriter.addPage(pdfReader.getPage(pageNum))

                        pdfWriter.write(outPdfFile)

                        # remove the encrypted file
                        os.remove(os.path.join(currentFolder, subFile))
                else:
                    print("Can not decrypt ->",
                          os.path.join(currentFolder, subFile))
                    continue
