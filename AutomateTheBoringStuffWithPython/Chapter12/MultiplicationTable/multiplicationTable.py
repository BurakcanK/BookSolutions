""" Multiplication Table Maker

This program takes a number N from the command line and creates an
N x N multiplication table in an Excel spreadsheet.

Usage:
    python3 multiplicationTable.py N
"""

from openpyxl import Workbook
from openpyxl.styles import Font
import sys

if len(sys.argv) != 2:
    print("Usage: python3 multiplicationTable.py N")

# create a workbook
wb = Workbook()
# select the active worksheet
ws = wb.active

# make the first row and column bold
ws.column_dimensions['A'].font = ws.row_dimensions[1].font = Font(bold=True)

# append the first row header
headers = [''] + [i for i in range(1, int(sys.argv[1]) + 1)]
ws.append(headers)

# create the table
for row in range(1, int(sys.argv[1]) + 1):
    ws.append([i * row for i in headers])

# write the first column header
for i in range(1, int(sys.argv[1]) + 1):
    ws.cell(row=i + 1, column=1, value=headers[i])

# save the workbook
wb.save('multTable.xlsx')
