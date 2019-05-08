"""Blank Row Inserter

Given the interval, insert blank rows into the Excel file.

Usage:
    python3 blank_row_inserter.py <start_row> <num_of_blank_rows> <file>
"""

import openpyxl
import sys

# ensure usage
if len(sys.argv) != 4:
    print("python3 blank_row_inserter.py <start_row> <num_of_blank_rows> <file>")
    sys.exit()

# load workbook, select active sheet
wb = openpyxl.load_workbook(sys.argv[3])
ws = wb.active

# insert blank rows
ws.insert_rows(int(sys.argv[1]), amount=int(sys.argv[2]))

wb.save(sys.argv[3])
