# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

multiples_of_3 = []
multiples_of_5 = []
for value in range(1, 1000):
    if (value % 3 == 0):
        multiples_of_3.append(value)
        continue # multiples of 3 and 5 must not be counted twice
    if (value % 5 == 0):
        multiples_of_5.append(value)

result = sum(multiples_of_3) + sum(multiples_of_5)
print("The solution is " + str(result))