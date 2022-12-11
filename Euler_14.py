# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

start_time = time.time()

result = 0
max_number_of_steps = 0

number_of_steps = {1: 1}

MAX_NUMBER = 1_000_000

for i in range(2, MAX_NUMBER):
    curr_number = i
    curr_number_of_steps = 0
    while curr_number != 1:
        if curr_number % 2 == 0:
            curr_number /= 2
        else:
            curr_number = 3 * curr_number + 1
        curr_number_of_steps += 1
        if curr_number in number_of_steps.keys():
            curr_number_of_steps += number_of_steps[curr_number]
            break
    if curr_number_of_steps > max_number_of_steps:
        max_number_of_steps = curr_number_of_steps
        result = i
    number_of_steps[i] = curr_number_of_steps

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))