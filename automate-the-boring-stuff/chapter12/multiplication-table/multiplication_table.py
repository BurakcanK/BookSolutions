"""Multiplication Table Maker

Take a number N from the command line and creat an
N x N multiplication table in an Excel spreadsheet.

Usage:
    python3 multiplication_table.py N
"""

import os
import sys
from openpyxl import Workbook
from openpyxl.styles import Font

if len(sys.argv) != 2:
    print("Usage: python3 multiplication_table.py N")

# create a workbook and select active worksheet
wb = Workbook()
ws = wb.active

# make the first row and column bold
ws.column_dimensions["A"].font = ws.row_dimensions[1].font = Font(bold=True)

# append the first row header
headers = [""] + [i for i in range(1, int(sys.argv[1]) + 1)]
ws.append(headers)

# create the table
for row in range(1, int(sys.argv[1]) + 1):
    ws.append([i*row for i in headers])

# write the first column header
for i in range(1, int(sys.argv[1]) + 1):
    ws.cell(row=i+1, column=1, value=headers[i])

# save the workbook
wb.save(os.path.join(
    os.path.dirname(__file__),
    "mult_table.xlsx")
)
