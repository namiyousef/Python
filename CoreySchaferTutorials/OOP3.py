#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 00:17:50 2020

@author: yousefnami
"""

# Video link: https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3

# Definitions:
# class methods: ensures that the function received the class as the first argument to the function (i.e. cls)
# static methods: static methods don't pass self or cls into the function, so they are like reg. functions
# except that they are included in the class, because they have some 'logical' connection to class
# regular methods: takes the class instance as the first argument to the function (i.e. self)
# alternative constructors: use class methods to provide multiple ways of creating objects

class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self,name,surname,pay):
        self.name = name 
        self.surname = surname 
        self.email = '{}.{}@hotmail.com'.format(name,surname)
        self.pay = pay
        Employee.num_of_emps += 1 # adds 1 each time a new class is instantiated! 
        
    def display_fullname(self):
        print('{} {}'.format(self.name,self.surname))
        
    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount
        print(self.pay)
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
        
        
Employee.set_raise_amount(200)
print(Employee.raise_amount)

Employee.raise_amount = 1.04
print(Employee.raise_amount)


# funnily enough, you can also run class methods from instances, but typically this is not done
# i.e. (having defined emp_1 first)... emp_1.set_raise_amount(value)

# Problem:
"""
suppose you've written a class that does a certain number of things very well, but then, someone who is 
using your class has inputs that aren't in the format required by your class.
see below:
"""

emp_1 = 'Yousef,Nami,7000'
emp_2 = 'Mohammad,Nami,2000'
# suppose for example you got your data from a CSV

# you wuld have to split them like this
data_1 = emp_1.split(',')
data_2 = emp_2.split(',')

emp_1 = Employee(*data_1)
emp_2 = Employee(*data_2)

print(emp_1.email)
print(emp_2.email)

#ideally, we would want our class to be able to do this for them. i.e. to
#instantiate a class based on a weird input that we weren't expecting when designing the class in the
# first place !

# redefine class

class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self,name,surname,pay):
        self.name = name 
        self.surname = surname 
        self.email = '{}.{}@hotmail.com'.format(name,surname)
        self.pay = pay
        Employee.num_of_emps += 1 # adds 1 each time a new class is instantiated! 
        
    def display_fullname(self):
        print('{} {}'.format(self.name,self.surname))
        
    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount
        print(self.pay)
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls,emp_str):
        emp_data = emp_str.split(',') # creates a local variable
        return cls(*emp_data) # instantiates the __init__!
        # must ave return, because it returns the instantiated class !
        

# so:
emp_1 = 'Yousef,Nami,7000'
emp_2 = 'Mohammad,Nami,2000'    

emp_1 = Employee.from_string(emp_1)
emp_2 = Employee.from_string(emp_2)

print(emp_1.email)
print(emp_2.email)



class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self,name,surname,pay):
        self.name = name 
        self.surname = surname 
        self.email = '{}.{}@hotmail.com'.format(name,surname)
        self.pay = pay
        Employee.num_of_emps += 1 # adds 1 each time a new class is instantiated! 
        
    def display_fullname(self):
        print('{} {}'.format(self.name,self.surname))
        
    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount
        print(self.pay)
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls,emp_str):
        emp_data = emp_str.split(',') # creates a local variable
        return cls(*emp_data) # instantiates the __init__!
        # must ave return, because it returns the instantiated class !
    
    @staticmethod

    def is_work_day(day):
        """
        how to tell if a function is a static method? Typically they don't have any reference to self or cls 
        """
        if day.weekday() == 5 or day.weekday() == 6:
            print(False)
        else:
            print(True)
           
import datetime as dt
date = dt.date(2016,7,11)

Employee.is_work_day(date)