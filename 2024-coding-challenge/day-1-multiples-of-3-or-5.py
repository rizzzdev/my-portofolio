'''
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once.

'''

# Solution
def solution(number):
    if number < 0 :
        return 0
    else:
        multiples_3 = [3*i for i in range(1, number + 1) if 3*i < number]
        multiples_5 = [5*i for i in range(1, number + 1) if 5*i < number]
        print(set(multiples_3 + multiples_5))

# Testing
print(solution(10))