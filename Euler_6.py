# The sum of the squares of the first ten natural numbers is,

# 1**2 + 2**2 + ... + 10**2 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)**2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 

# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time
start_time = time.time()

target_number = 100

squares = [value**2 for value in range(1, target_number + 1)]
numbers = range(1, target_number + 1)

sum_of_squares = sum(squares)
square_of_sums = sum(numbers)**2

result = abs(sum_of_squares - square_of_sums)
print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))