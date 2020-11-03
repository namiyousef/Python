"""
Author: Yousef Nami
Problem definition: https://leetcode.com/problems/regular-expression-matching/
Date started: 27.10.2020
Date complete: 
Results: 

"""

def reg_ex_matching(s, p):
    if p[-1] != s[-1] and p[-1] not in '*.':
        return False
    
    j = 0
    letter = ""
    for i in p:
        if i == '*':
            k = 0
            while s[j] != letter[-1]:
                
                if s[j] != letter[k] and s[j] != '.':
                    if j == 0:
                        break
                    else:
                        return False
                k += 1
                j += 1
                
            while j < len(s) and (s[j] == letter[-1] or letter[-1] == '.'):  
                j += 1
            
            letter = ""
        else:
            
            letter += i
      
    l = len(letter)
    if p[-1] not in '*.':
        for i in range(0,l):
            if s[i-1] != letter[i-1] and letter[i-1] != '.':
                return False
    
    if j == 0:
        if '.' not in p:
            return s == p
        if len(p) != len(s):
            return False
    
        
    
    return True
            
            
print(reg_ex_matching('aa','a')) # false
print(reg_ex_matching('aa','a*')) #true 
print(reg_ex_matching('ab','.*')) # true 
print(reg_ex_matching('aab','c*a*b')) # ture
print(reg_ex_matching('mississippi','mis*is*p*.')) # false
print(reg_ex_matching('mississippi','mis*is*ip*.')) # true
print(reg_ex_matching("ab",".*c")) # false
print(reg_ex_matching("aaa","a.a")) # true
print(reg_ex_matching("aaa","ab*ac*a")) # true

