"""PDF Paranoia Decrypt

Find all of the PDF files in a directory, decrypt them using the password
provided on the command line and save each decrypted PDF with an "_decrypted.pdf" suffix.
If decryption fails, inform the user and proceed to the next pdf file.

Usage:
    python3 pdf_decrypt.py <folder> <password>
"""

import os
import PyPDF2
import sys

# ensure usage
if len(sys.argv) != 3:
    print("Usage: python3 pdf_decrypt.py <folder> <password>")
    sys.exit()

# walk through the files
for current_folder, _, sub_files in os.walk(sys.argv[1]):
    for sub_file in sub_files:
        # find and decrypt the pdf files
        if sub_file.endswith(".pdf"):
            # try to decrypt the encrypted file
            with open(os.path.join(current_folder, sub_file), "rb") as in_pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(in_pdf_file)

                # decryption successful
                if pdf_reader.decrypt(sys.argv[2]) == 1:
                    with open(os.path.join(current_folder, sub_file[:-4] + "_decrypted.pdf"), "wb") as out_pdf_file:
                        pdf_writer = PyPDF2.PdfFileWriter()

                        # add all pages to the outfile
                        for page_num in range(pdf_reader.getNumPages()):
                            pdf_writer.addPage(pdf_reader.getPage(page_num))

                        pdf_writer.write(out_pdf_file)

                        # remove the encrypted file
                        os.remove(os.path.join(current_folder, sub_file))
                else:
                    print("Can not decrypt ->",
                          os.path.join(current_folder, sub_file))
                    continue
