""" Blank Row Inserter

Given the interval, this script inserts blank rows into the Excel file.

Usage:
    python3 blankRowInserter.py <startRow> <numOfBlankRows> <file>
"""

import openpyxl
import sys

# ensure usage
if len(sys.argv) != 4:
    print("Usage: python3 blankRowInserter.py <startRow> <numOfBlankRows> <file>")
    sys.exit()

# load workbook, select active sheet
wb = openpyxl.load_workbook(sys.argv[3])
ws = wb.active

# insert blank rows
ws.insert_rows(int(sys.argv[1]), amount=int(sys.argv[2]))

wb.save(sys.argv[3])
