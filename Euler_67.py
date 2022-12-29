# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
# from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem
# 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)

import time


def read_file():
    with open('files/input_67.txt') as f:
        return f.readlines()


def f_all_arrays():
    numbers = []
    for line in read_file():
        numbers_as_strings = line.split()
        numbers_as_numbers = list(map(lambda x: int(x), numbers_as_strings))
        numbers.append(numbers_as_numbers)
    return numbers


def append_to_array(array, appendix):
    array.append(appendix)
    return array


start_time = time.time()
all_arrays = f_all_arrays()

curr_numbers = all_arrays[0]
# remove comments to get the actual directions
#curr_directions = [['s']]
next_numbers = []
#next_directions = []

for row_num in range(1, len(all_arrays)):
    next_numbers = []
    #next_directions = []
    for col_num in range(0, len(all_arrays[row_num])):
        if col_num == 0:
            # first number, always add with first number from row above
            next_numbers.append(all_arrays[row_num][0] + curr_numbers[0])
            #next_directions.append(append_to_array(curr_directions[0][:], 'l'))
        elif col_num == len(all_arrays[row_num]) - 1:
            # last number, always add with last number from row above
            next_numbers.append(all_arrays[row_num][col_num] + curr_numbers[-1])
            #next_directions.append(append_to_array(curr_directions[-1][:], 'r'))
        elif curr_numbers[col_num - 1] >= curr_numbers[col_num]:
            next_numbers.append(all_arrays[row_num][col_num] + curr_numbers[col_num - 1])
            #next_directions.append(append_to_array(curr_directions[col_num - 1][:], 'r'))
        else:
            next_numbers.append(all_arrays[row_num][col_num] + curr_numbers[col_num])
            #next_directions.append(append_to_array(curr_directions[col_num][:], 'l'))
    #curr_directions = next_directions
    curr_numbers = next_numbers

result = max(curr_numbers)
#print(curr_directions[curr_numbers.index(result)])

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
