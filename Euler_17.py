# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage.

import time

NUMBER_TO_WORDS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000: "onethousand"
}


def to_word(x):
    if x == 1000:
        return NUMBER_TO_WORDS.get(x)
    if x < 100:
        return to_tens(x)
    return to_hundred(x)


def to_hundred(x):
    num_of_hundreds = int(x / 100)
    hundreds = NUMBER_TO_WORDS.get(num_of_hundreds) + "hundred"
    if x % 100 == 0:
        return hundreds
    else:
        return hundreds + "and" + str(to_tens(x - 100 * num_of_hundreds))


def to_tens(x):
    if x == 0:
        return ''
    elif x <= 20:
        return NUMBER_TO_WORDS.get(x)
    elif x % 10 == 0:
        return str(NUMBER_TO_WORDS.get(x))
    elif x < 100:
        return str(NUMBER_TO_WORDS.get(int(x / 10) * 10)) + str(NUMBER_TO_WORDS.get(x % 10))


start_time = time.time()
result = 0
for i in range(1, 1001):
    result += len(to_word(i))

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
