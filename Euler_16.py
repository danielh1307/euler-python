# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2**1000?

import time

start_time = time.time()

EXPONENT = 1000
x = str(2**EXPONENT)
result = 0
for i in range(0, len(x)):
    result += int(x[i])

print("The solution is " + str(result))
print("--- %s seconds ---" % (time.time() - start_time))
