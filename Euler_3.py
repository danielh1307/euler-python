# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600_851_475_143 ?

import math
from Euler_Functions import is_prime

target_number = 600_851_475_143

result = 1
value = 1
while True:
    value += 1
    result_of_division = target_number / value # we do not take the modulo here since otherwise we are doing the division twice

    if (not result_of_division.is_integer()): # check if result_of_division is a whole number
        continue;

    # now we know result_of_division is a whole number --> that means value is a factor of target_number
    if (is_prime(value)):
        result = value
    target_number = int(result_of_division)
    if (target_number == 1):
        break

print("The solution is " + str(result))