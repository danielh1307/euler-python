# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(x):
    return str(x) == str(x)[::-1]

three_digit_numbers = list(range(100, 1000))
result = 0
for first_number in three_digit_numbers:
    for second_number in three_digit_numbers:
        product = first_number * second_number
        if (product > result and is_palindrome(product)): 
            result = product

print("The solution is " + str(result))
