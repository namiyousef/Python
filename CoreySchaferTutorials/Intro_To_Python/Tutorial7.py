#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:46:49 2020

@author: yousefnami
"""

nums = [1,2,'test',4,5,6]

for i in range(len(nums)):
    if isinstance(nums[i],str):
        print('fuck')
        
#if you do:
for num in nums:
    print(num)

#you're actually looping through the items in the list, not the indices!
#so:
for num in nums:
    if isinstance(num,str):
        print('fuck')
        break #causes the loop to stop!
    
#continue causes you to skip an iteration
for num in nums:
    if isinstance(num,str):
        continue
    print(num)
#as we can see, only the numbers have been printed!