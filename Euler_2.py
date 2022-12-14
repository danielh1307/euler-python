# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#   1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fibonacci_numbers = [1, 2]
result = 2

# start with creating all Fibonacci numbers
while True:
    new_fibonacci = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    fibonacci_numbers.append(new_fibonacci)
    if (new_fibonacci % 2 == 0):
        result += new_fibonacci
    if new_fibonacci >= 4_000_000:
        break

print("The solution is " + str(result))