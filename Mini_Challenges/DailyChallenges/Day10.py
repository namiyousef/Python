"""
Author: Yousef Nami
Problem definition: https://leetcode.com/problems/palindrome-number/
Date started: 26.10.2020
Date complete: 26.10.2020
Results: 
    - faster than 58%
    - lower in memory than 98%

"""


def check_palindrome(x):
    if x < 0:
        return False
    dig = []
    while x != 0:
        dig.append(x%10)
        x = x//10
    
    for i in range(len(dig)//2):
        if dig[i] != dig[len(dig) - i - 1]:
            return False
    return True
    
print(check_palindrome(1001))