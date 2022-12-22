# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import time


def factorial(x):
    if x == 1:
        return x

    return x * factorial(x - 1)


start_time = time.time()

n = factorial(100)
result = 0
for i in str(n):
    result += int(i)

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
