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


def get_factors(number, with_number=True):
    factors = [1]
    if number == 1:
        return factors

    for i in range(2, int(math.sqrt(number)) + 1):
        if i in factors:
            break

        r = number / i
        if is_natural_number(r):
            factors.append(int(r))
            if r != i:
                factors.append(int(i))

    if with_number:
        factors.append(number)

    factors.sort()
    return factors


def is_natural_number(n):
    return math.floor(n) == n