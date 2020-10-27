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
            #for k in range(j, j+l):
            #    if s[k] != letter[k-j] and s[k] != '.':
            #        if j == 0:
            #            break
            #        else:
            #            return False
            #p = 0
            #while k + p < len(s) - 2 and s[k + p] != letter[-1]:
            #    p += 1
            
            
            #j += l + p
            
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