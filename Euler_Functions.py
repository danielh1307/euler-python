import math


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for value in range(2, int(math.sqrt(number)) + 1):
        if number % value == 0:
            return False
    return True
