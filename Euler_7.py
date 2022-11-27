# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import time
from Euler_Functions import is_prime

start_time = time.time()

result = 0
i = 0
while True:
    result += 1
    if (is_prime(result)):
        i += 1
        if (i == 10_001):
            break

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))