# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# (Answer is 232792560 but the solution takes a lot of time ~56s)

result = 1
while True:
    num_of_divisors = 0
    result += 1
    for i in range(11, 21):
        if (result % i == 0):
            num_of_divisors += 1
        else:
            break
    # print(f"{result} and {num_of_divisors}")
    if (num_of_divisors == 10):
        break

print("The solution is " + str(result))