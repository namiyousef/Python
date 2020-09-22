#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:11:33 2020

@author: yousefnami
"""

#Tutorial 5: dictoinaries and key-value pairs

student = {'name': 'John', 'age': 25, 'courses': ['Math','CompSci']} #curly brackets starts dictionary
print(student)
print(student['name']) #this is very useful eh? 
#the key 'name' in the student dictionary can also be an integer...
print(student.get('name'))
print(student.get('test')) #returns  none since a 'test' key does not exist!
print(student.get('test',69)) #returns 69 if test not found 

#can also add keys!

student['death'] = 'no'
print(student)
#can also update values
student['name'] = 'Jane'
student.update({'name':'John', 'death': 'yes'})
print(student)

age = student.pop('age')
#del student['age'] #gives error because it no longer exists since pop took it away!
print(age)
print(student.keys())
print(student.values())
print(student.items())

#for looping

for key, value in student.items():
    print(key,value)
    