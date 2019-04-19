"""Table Printer

Display a given list of lists of items with each column right justified.
"""


def print_table(table):
    # create a list of zeros
    col_widths = [0] * len(table)

    # decide the column width of each column
    for i in range(len(table)):
        col_widths[i] = len(max(table[i], key=len))

    # print the table right justified
    for row in range(len(table[0])):
        for col in range(len(table)):
            print(table[col][row].rjust(col_widths[col]), " ", end="")
        print()


table_data = [["apples", "oranges", "cherries", "banana"],
              ["Alice", "Bob", "Carol", "David"],
              ["dogs", "cats", "moose", "goose"]]

print_table(table_data)
