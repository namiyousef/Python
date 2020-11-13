"""
Author: Yousef Nami
Problem definition: https://leetcode.com/problems/integer-to-roman/
Date started: 13.11.2020
Date complete: 
Results:
    
"""

def int_to_roman(num):
    romans = ['M','D','C','L','X','V','I']
    roman_int = 1000
    divisors = [2,5]
    init = 1
    num_roman = '';
    for i in range(len(romans)):
        n_romans = int(num//roman_int)
        print(num, roman_int)
        print(n_romans)
        if i != 0:
            num_roman += (romans[i]+romans[i-1]) if n_romans == 4 else (romans[i]+romans[i-2]) if n_romans == 9 else romans[i]*n_romans
        num -= n_romans*roman_int
        init = 1 - init
        roman_int /= divisors[init]
        
    return num_roman


print(int_to_roman(3))
print(int_to_roman(4))
print(int_to_roman(9)) # this is wrong
print(int_to_roman(58))

# NOTE: this will not work perfectly, you need to make a dict and interate through the dict
# this isn't that hard, you got this