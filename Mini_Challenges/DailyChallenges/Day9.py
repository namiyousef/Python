"""
Author: Yousef Nami
Problem definition: https://leetcode.com/problems/string-to-integer-atoi/
Date started: 23.10.2020
Date complete: 
Results: 
"""



def convert_to_int(s = '1234'):
    digits = "0123456789- "
    if not s:
        return 0
    num = ""
    for letter in s:
        if letter not in digits:
            num = 0 if (not num or num=='-') else num
            break
        elif letter != " ":
            num+=letter
    print(num)    
    num = 2**31 - 1 if int(num) > 2**31 -1 else int(num)
    num = -2**31 if int(num) < -2**31 else int(num)
    return num

convert_to_int(
"")

if "":
    print('test')