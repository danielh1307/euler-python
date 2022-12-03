# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import time

from Euler_Functions import is_prime

start_time = time.time()
result = 0
for i in range(1, 2_000_000):
    if is_prime(i):
        result += i
    i += 1

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))