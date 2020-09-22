#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 11:15:59 2020

@author: yousefnami
"""

def hello(greeting, name ='You'): #sets name by default, can be changed!
    return '{} {}'.format(greeting,name)
    pass #allows you to set a function without actually putting something in it


print(hello('Hi'))
print(hello('Hi','Aida'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math','Art', name = "John", age = "25") #QUESTION: why does it generate a tuple? What if I want to generate somethig mutable? 

#the * and ** make sure that you 'unpack' values

#for example:

courses = ['math','art'] 
info = {'name':'John','age':25}
student_info(courses,info) #as shown, this does not work out!

#so:
student_info(*courses,**info)