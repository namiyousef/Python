"""
Author: Yousef Nami
Problem definition: https://leetcode.com/problems/longest-palindromic-substring/
Constraints:
    - input string length bounded by 1 and 1000
    - consists of lower and upper case chars
Date started: 20.10.2020
Date complete: 20.10.2020
Results:
"""

def find_palindrome(s = '1234'):
    for j in range(int(len(s)/2)):
       for i in range(j,len(s)):
           #print(s[i:len(s)-j],j)
           print(s[j:len(s)-i],j)
           #if check_palindrome(s[i:len(s)-j]):
           #    return s[i:len(s)-j]
           #elif check_palindrome(s[j:len(s)-i]):
           #    return s[j:len(s)-i]
 
print(find_palindrome('cbbd'))

def check_palindrome(s):
    l = len(s) 
    for i in range(int(l/2)):
        if s[i] != s[l-i-1]:
            return False
    return True
        
    
print(check_palindrome('23834892'))
