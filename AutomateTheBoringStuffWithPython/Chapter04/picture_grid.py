"""Character Picture Grid

Print a characterized image.
"""

grid = [[".", ".", ".", ".", ".", "."],
        [".", "0", "0", ".", ".", "."],
        ["0", "0", "0", "0", ".", "."],
        ["0", "0", "0", "0", "0", "."],
        [".", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "."],
        ["0", "0", "0", "0", ".", "."],
        [".", "0", "0", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]]

# print every row in every column
for col in range(len(grid[0])):
    for row in range(len(grid)):
        print(grid[row][col], end = "")
    print()
