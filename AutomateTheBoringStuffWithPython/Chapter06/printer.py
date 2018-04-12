""" Table Printer

Displays a given list of lists of items with each column right justified.
"""

def printTable(table):
    # create a list of zeros
    colWidths = [0] * len(table)

    # decide the column width of each column
    for i in range(len(table)):
        colWidths[i] = len(max(table[i], key = len))

    # print the table right justified
    for row in range(len(table[0])):
        for col in range(len(table)):
            print(table[col][row].rjust(colWidths[col]), " ", end = "")
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
