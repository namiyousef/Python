"""
Author: Yousef Nami
Problem definition: https://leetcode.com/problems/regular-expression-matching/
Date started: 27.10.2020
Date complete: 
Results: 

"""

def reg_ex_matching(s, p):
    
    j = 0
    letter = ""
    for i in p:
        
        if i == '*':
            l = len(letter)
            
            for k in range(j, j+l):
                if s[k] != letter[k-j] and s[k] != '.':
                    if j == 0:
                        break
                    else:
                        return False
                    
           # if s[j:j+l] != letter:
           #     if j == 0:
           #         break
           #     else:
           #         return False
            
            
            j += l
            
            letter = ""
                    
        else:
            
            letter += i
       
      
    if j == 0:
        return s == p
    
    return True
            
            
print(reg_ex_matching('aa','a'))
print(reg_ex_matching('aa','a*'))
print(reg_ex_matching('ab','.*'))
print(reg_ex_matching('aab','c*a*b'))
print(reg_ex_matching('mississippi','mis*is*p*.'))
print(reg_ex_matching('mississippi','mis*is*ip*.'))