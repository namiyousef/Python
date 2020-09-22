#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:24:41 2020

@author: yousefnami
"""

#Conditionals

#'is' is useful to check if somethinh is the same thing in memory!

#for example:

test = [1,2,3]
test2= test
print(test is test2) #this prints true, because remember that unlike otherlanguages, putting 
#test 2 = test does not set a new variable! 
#however:
test3= test.copy()
print(test is test3)
print('values that python interprets as false all the time')

condition = False
if not condition: #not is there, because python only executes 'true' code
    print('False')
condition = None
if not condition:
    print('False')
condition = 0
if not condition:
    print('False')
    
condition = ''
if not condition:
    print('False')
    
condition = ()
if not condition:
    print('False')

condition = []
if not condition:
    print('False')
    
condition = {}
if not condition:
    print('False')