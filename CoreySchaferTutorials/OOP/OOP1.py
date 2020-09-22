#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:38:26 2020

@author: yousefnami
"""

# Link to video: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

# This video deals with the basics of classes. Note that I'd been introduced to classes prior to watching this video

# Definitions:
# Methods: a function that is associated with a class
# Attributes: things that you define in a class that are 'specific to the class', i.e. self.name
# Class instance: this is when you define a variable as a class (which creates an 'instance' of the class)


# Introduction
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print((emp_1,emp_2))

# you can add attributes to a class before actually defining them in the class

# so as an example:

emp_1.first = 'Yousef'

print(emp_1.first)

# with intialising

class Employee:
    def __init__(self,name,surname,pay):
        self.name = name 
        self.surname = surname 
        self.email = '{}.{}@hotmail.com'.format(name,surname)
        self.pay = pay
        
    def display_fullname(self):
        """ note: when defining functions in a class, you must have the 'self' variable
        the reason for this is that, when you refer to the method, i.e. class_instance.method() you
        are inputting the class_instance as an input intot he function. So if you define it without
        taking any inputs, then the error would be method() takes no arguments but 1 was given """
        print('{} {}'.format(self.name,self.surname))
        
user_data = ['Yousef','Nami','50000']
emp_1 = Employee(*user_data)

print(emp_1.email)

emp_1.display_fullname() 

# Note, you must put the parenthesis, because otherwise it would refer to the memory location of the 
# method 'fullname'. If you put () when you actually run the method


# a nice comparison

Employee.display_fullname(emp_1)

emp_1.display_fullname() 

# both of he above do the same thing. This explains the comment in green above a bit better. 
# when you refer to the method as an addition to the class instance, so emp_1.display_fullname()
# then you implicitly give it an input of emp_1

# when you refer to the class first, then give it an instance, then the instance that you give it 
# is interpreted as 'self'








