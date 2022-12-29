# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first
# names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply
# this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is
# the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

import time


def get_sorted_names():
    with open('files/input_22.txt') as f:
        file_line = f.readline().replace('"', '')

    names = file_line.split(',')
    names.sort()
    return names


start_time = time.time()

alphabetical_values = {}
for i in range(ord('A'), ord('Z') + 1):
    alphabetical_values[chr(i)] = i - 64

sorted_names = get_sorted_names()
result = 0
for i in range(0, len(sorted_names)):
    alphabetical_value = 0
    for letter in sorted_names[i]:
        alphabetical_value += alphabetical_values[letter]
    result += alphabetical_value * (i + 1)

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
