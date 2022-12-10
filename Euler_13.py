# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import time


def read_file():
    with open('files/input_13.txt') as f:
        return f.readlines()


def sum_numbers(numbers):
    """We expect all numbers have the same number of figures"""
    t_sum = ''
    rest = 0
    for i in range(0, len(numbers[0].strip())):
        index = -1 - i
        sum_of_figures = rest
        for number in numbers:
            sum_of_figures += int(number.strip()[index])

        t_sum = str(sum_of_figures % 10) + t_sum
        rest = int(sum_of_figures / 10)

    if rest != 0:
        t_sum = str(rest) + t_sum
    return t_sum


start_time = time.time()

numbers = read_file()

result = sum_numbers(numbers)

print("The solution is " + str(result[0:10]))
print("--- %s seconds ---" % (time.time() - start_time))
