'''

https://www.codewars.com/kata/526571aae218b8ee490006f4

DESCRIPTION:
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

'''

# Solution
# def count_bits(n):
#     return bin(n).replace("0b", '').count('1')
count_bits = lambda n : bin(n).replace("0b", '').count('1')

# Testing
print(count_bits(1234))