'''

https://www.codewars.com/kata/525f50e3b73515a6db000b83

DESCRIPTION:
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!

'''

# Solution
def create_phone_number(n):
    str_n = ''.join([str(i) for i in n])
    return f'({str_n[0:3]}) {str_n[3:6]}-{str_n[6:]}'

# Testing
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))