# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import time

start_time = time.time()

SPIRAL = 1001
down_times = result = counter = 1
left_up_right_times = 2

# starting at 1
# 1 right, 1 down
# 2 left, 2 up, 2 right
# 1 right, 3 down
# 4 left, 4 up, 4 right
# 1 right, 5 down
# 6 left, 6 up, 6 right
while left_up_right_times < SPIRAL:
    counter += 1  # one step right
    for i in range(down_times):  # here we go down
        counter += 1
    result += counter  # number at the bottom right
    for i in range(3):  # now we go left, up, right
        for j in range(left_up_right_times):  # number of times
            counter += 1
        result += counter  # number at the bottom left, top left, top right
    down_times += 2
    left_up_right_times += 2

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
