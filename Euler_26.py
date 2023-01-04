# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2
# to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
# cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import time


def get_recurring_cycle(divisor):
    r = '.'
    dividend = 1
    all_divisors = []
    while True:
        first_step = True
        while dividend < divisor:
            dividend *= 10
            if first_step:
                first_step = False
            else:
                r += '0'

        if dividend % divisor == 0:
            return '0', '0'  # there is no cycle

        rest = dividend // divisor
        if dividend in all_divisors:
            return r, str(rest)  # we have found a recurring cycle

        all_divisors.append(dividend)
        r += str(rest)

        dividend -= (divisor * rest)


def get_repeating_structure(t):
    return t[0][t[0].index(t[1]):len(t[0])]


start_time = time.time()

longest_cycle = 0
result = 0
for i in range(1, 1000):
    rep_structure = get_repeating_structure(get_recurring_cycle(i))
    if len(rep_structure) > longest_cycle:
        longest_cycle = len(rep_structure)
        result = i

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))