# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?

import time


def get_row_pascal_triangle(row_num):
    """The problem can be expressed like: get me the middle number of a specific row in Pascal's triangle"""
    curr_row = [1]
    for i in range(1, row_num):
        next_row = []
        for j in range(0, len(curr_row) + 1):
            if j == 0 or j == len(curr_row):
                # first and last element are 0
                next_row.append(1)
            else:
                next_row.append(curr_row[j - 1] + curr_row[j])
        curr_row = next_row

    return curr_row


start_time = time.time()

NUM_OF_GRIDS = 20
ROW = NUM_OF_GRIDS * 2 + 1  # always an odd number --> there is always an exact "middle" number
INDEX = int((ROW - 1) / 2)  # INDEX now represents the index of the number left to the middle (starting by 1)

result = get_row_pascal_triangle(ROW)[INDEX]  # since first element has index=0 we are taking the middle here

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
