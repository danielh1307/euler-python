# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import time

start_time = time.time()

NUM_OF_DIGITS = 1000

last_fibonacci = 0
curr_fibonacci = 1
result = 1
while True:
    if len(str(curr_fibonacci)) >= NUM_OF_DIGITS:
        break
    curr_fibonacci += last_fibonacci
    last_fibonacci = curr_fibonacci - last_fibonacci
    result += 1

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
