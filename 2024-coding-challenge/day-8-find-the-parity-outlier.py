'''

https://www.codewars.com/kata/5526fc09a1bbd946250002dc

DESCRIPTION:
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

'''

# Solution
def find_outlier(integers):
    mod_arr = [abs(i % 2) for i in integers]
    if mod_arr.count(1) > mod_arr.count(0):
        return integers[mod_arr.index(0)]
    else:
        return integers[mod_arr.index(1)]

# Testing
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))