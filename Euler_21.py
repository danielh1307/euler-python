# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
# numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import time
from Euler_Functions import get_factors


start_time = time.time()

d = {}
amicable = []
for i in range(1, 10001):
    if i not in d.keys():
        d[i] = sum(get_factors(i, False))
    if d[i] > 10000:
        continue
    if d[i] not in d.keys():
        d[d[i]] = sum(get_factors(d[i], False))
    if d[d[i]] == i and i != d[i]:
        amicable.append(i)

result = sum(amicable)

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))


