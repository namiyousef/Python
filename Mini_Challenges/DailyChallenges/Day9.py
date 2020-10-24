"""
Author: Yousef Nami
Problem definition: https://leetcode.com/problems/string-to-integer-atoi/
Date started: 23.10.2020
Date complete: 24.10.2020
Results: 
    - faster than 55.6% of submissions
    - less memory than 99.98% of submissions
"""



def convert_to_int(s = '1234'):
    digits = "0123456789-+ "
    if not s:
        return 0
    num = ""
    i = 0
    while i<len(s) and s[i] in digits:
        if s[i] != " ":
            digits = digits[:10]
            num += s[i]
        i += 1
        
    try:
        num = int(num)
        num = 2**31 - 1 if num > 2**31 -1 else num
        num = -2**31 if num < -2**31 else num
    except:
        return 0
    print(num)
    return num

convert_to_int(
"4193 with words")