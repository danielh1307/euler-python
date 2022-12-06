# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
# (see input files/input_11.txt)
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

import time
import math

GRID_SIZE = 20


def read_file():
    with open('files/input_11.txt') as f:
        return f.readlines()


def get_all_rows(f_input):
    rows = []
    for row_num in range(0, GRID_SIZE):
        row_in_strings = f_input[row_num].split()
        rows.append(list(map(lambda x: int(x), row_in_strings)))

    return rows


def get_all_cols(all_rows):
    cols = []  # two-dimensional array
    for col_num in range(0, GRID_SIZE):
        col_array = []
        for row_num in range(0, len(all_rows)):
            col_array.append(all_rows[row_num][col_num])
        cols.append(col_array)

    return cols


def get_diagonal_right(rows):
    return_values = []
    r = c = 0
    while r + 3 < GRID_SIZE:
        if c + 3 < GRID_SIZE:
            return_values.append([rows[r][c], rows[r + 1][c + 1], rows[r + 2][c + 2], rows[r + 3][c + 3]])
            c += 1
        if c + 3 == GRID_SIZE:
            r += 1
            c = 0

    return return_values


def get_diagonal_left(rows):
    return_values = []
    r = 0
    c = 19
    while r + 3 < GRID_SIZE:
        if c - 3 >= 0:
            return_values.append([rows[r][c], rows[r + 1][c - 1], rows[r + 2][c - 2], rows[r + 3][c - 3]])
            c -= 1
        if c - 3 < 0:
            r += 1
            c = 19

    return return_values


start_time = time.time()

result = 0

all_rows = get_all_rows(read_file())

for row in all_rows:
    for i in range(0, GRID_SIZE - 3):
        result = max(result, math.prod(row[i:i+4]))

for col in get_all_cols(all_rows):
    for i in range(0, GRID_SIZE - 3):
        result = max(result, math.prod(col[i:i+4]))

for diagonal in get_diagonal_right(all_rows):
    result = max(result, math.prod(diagonal))

for diagonal in get_diagonal_left(all_rows):
    result = max(result, math.prod(diagonal))

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
