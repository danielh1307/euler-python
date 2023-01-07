# Euler discovered the remarkable quadratic formula: n**2 + n + 41
#
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
#
# The incredible formula n**2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values .
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form: n**2 + an + b
#
# , where  |a| < 1000 and |b| < 1000

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
# for consecutive values of , starting with n = 0.

import time
from Euler_Functions import is_prime


def num_of_consecutive_primes(a, b):
    num = 0
    while True:
        if is_prime(num ** 2 + a * num + b):
            num += 1
        else:
            break
    return num


start_time = time.time()

result = 0
max_consecutive_primes = 0
for first_num in range(-999, 1000):
    for second_num in range(-1000, 1001):
        # for n = 0 and n = 1 we can test immediately
        if not is_prime(second_num) or \
                not is_prime(1 + first_num + second_num):
            continue
        consecutive_primes = num_of_consecutive_primes(first_num, second_num)
        if consecutive_primes > max_consecutive_primes:
            max_consecutive_primes = consecutive_primes
            result = first_num * second_num

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
