"""PDF Paranoia Encrypt

Find all of the PDF files in a directory, encrypt them using the password
provided on the command line and save each encrypted PDF with an "_encrypted.pdf" suffix.

Usage:
    python3 pdf_encrypt.py <folder> <password>
"""

import os
import PyPDF2
import sys

# ensure usage
if len(sys.argv) != 3:
    print("Usage: python3 pdf_encrypt.py <folder> <password>")
    sys.exit()

# walk through the files
for current_folder, _, sub_files in os.walk(sys.argv[1]):
    for sub_file in sub_files:
        # find and encrypt the pdf files
        if sub_file.endswith(".pdf"):
            # open a file for writing the encrypted pdf
            with open(os.path.join(current_folder, sub_file), "rb") as in_pdf_file,\
                    open(os.path.join(current_folder, sub_file[:-4] + "_encrypted.pdf"), "wb") as out_pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(in_pdf_file)
                pdf_writer = PyPDF2.PdfFileWriter()

                # add all pages to the outfile
                for page_num in range(pdf_reader.getNumPages()):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))

                pdf_writer.encrypt(sys.argv[2])
                pdf_writer.write(out_pdf_file)

            # make sure the encryption is successful before deletion
            with open(os.path.join(current_folder, sub_file[:-4] + "_encrypted.pdf"), "rb") as encrypted_file:
                pdf_reader = PyPDF2.PdfFileReader(encrypted_file)

                if pdf_reader.decrypt(sys.argv[2]) == 1:
                    os.remove(os.path.join(current_folder, sub_file))
