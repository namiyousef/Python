"""
Author: Yousef Nami
Problem definition: https://leetcode.com/problems/reverse-integer/
Date started: 23.10.2020
Date complete: 23.10.2020
Results: 
    - faster than 65.41% of users
    - less memory than 99.99% of users
"""

def reverse(x = -230):
    x, y = [str(x)[1:], "-"] if x<0 else [str(x), ""]
    
    for i in range(len(x)-1,-1,-1):
        y += x[i]
    return int(y)

