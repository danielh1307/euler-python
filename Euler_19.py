# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import time


def get_next_date(current_date):
    current_day = current_date[0]
    current_month = current_date[1]
    current_year = current_date[2]

    next_month = current_month
    next_year = current_year

    if current_day == 28 and current_month == 2:
        if is_schaltjahr(current_year):
            next_day = 29
        else:
            next_day = 1
            next_month = 3
    elif (current_day == 29 and current_month == 2) or \
            (current_day == 30 and current_month in (4, 6, 9, 11)) or \
            (current_day == 31 and current_month in (1, 3, 5, 7, 8, 10, 12)):
        next_day = 1
        if current_month == 12:
            next_month = 1
            next_year = current_year + 1
        else:
            next_month = current_month + 1
    else:
        next_day = current_day + 1

    return next_day, next_month, next_year


def is_schaltjahr(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


start_time = time.time()
result = 0
day_offset = 0
date = (1, 1, 1901)  # this day was a Tuesday - 6.1.1901 was the first Sunday in 1901
while date[2] < 2001:
    day_offset += 1
    if date[0] == 1 and (day_offset + 1) % 7 == 0:
        result += 1
    date = get_next_date(date)

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
