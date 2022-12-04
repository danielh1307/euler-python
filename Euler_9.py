# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a**2 + b**2 = c**2

# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time

# Idea: we define a < b < c
# We define both a and b
# from this we calculate c: 1000 - (a + b)
# We check if a**2 + b**2 == c**2
# if not, we increase a by one
# if a == b, we increase b by one and set a to the base again
# we do this until b is 500

start_time = time.time()
result = 0
base = 1
a = b = base

while b < 500:
    c = 1000 - (a + b)
    if a ** 2 + b ** 2 == c ** 2:
        result = a * b * c
        break
    if a < b:
        a += 1
    else:
        b += 1
        a = base

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
