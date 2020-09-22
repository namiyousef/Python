#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:59:48 2020

@author: yousefnami
"""

# Link to video: https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2

# Definitions:
# Class variables: variables that are the same for each instance
# Instance variables: variables that are specific to instances

class Employee:
    
    def __init__(self,name,surname,pay):
        self.name = name 
        self.surname = surname 
        self.email = '{}.{}@hotmail.com'.format(name,surname)
        self.pay = pay
        
    def display_fullname(self):
        print('{} {}'.format(self.name,self.surname))
        
    def apply_raise(self):
        self.pay = int(self.pay) * 1.04 # increases pay by 4%
        print(self.pay)
        
        
emp_1 = Employee('Yousef','Nami','50000')

emp_1.apply_raise()


# Problem: 
"""
If we want to have a constant raise (that isn't specific to each employee), we'd like it to be editable
Currently, by means of the hard-coded 1.04, it is NOT editable. So how can we create here, a class variable
so that it is shared bt all instances, and such that it can be updated?
"""

class Employee:
    
    raise_amount = 1.04
    pay = 1.05
    
    def __init__(self,name,surname,pay):
        self.name = name 
        self.surname = surname 
        self.email = '{}.{}@hotmail.com'.format(name,surname)
        self.pay = pay
        
    def display_fullname(self):
        print('{} {}'.format(self.name,self.surname))
        
    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount # note, must still refer to it by self! (can also be 
        # Employee.raise_amount, not necessarily self)
        print(self.pay)
    

"""
so, why is it possible to refer to raise_amount from self (i.e. from the instance!) when it is a class
variable? this is because when you use 'self', python first checks instance variables matching that name,
if it does not find any, then it moves to check class variables or inherited variables.
"""

# we can actually check this! SEE PAY as a class variable 

print(emp_1.__dict__)
print(Employee.__dict__)

print(emp_1.pay)
print(Employee.pay)

# as you can see, since now the 'pay' var exists in the class space AND the instance space, you have
# two different outcomes

# NOTE on updates:

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.06

emp_2  = Employee('Jo','Nami','50000')

print(Employee.raise_amount)
print(emp_2.raise_amount)
print(emp_1.raise_amount)

# Note how changing employee.raise_amount affected emp_2 as well, but changing emp_1.raise_amount ONLY
# affected emp_1

# this is because, as you learnt in lesson 1, you can define attributes outside the class space.
# doing emp_1.raise_amount = 1.06 essentially defined a self.raise_amount inside the class 
# it is only when the variable emp_1.raise_amount does not exist (i.e. if you are printing it) that it
# uses the class variable 


# as such, in the class method 'apply_raise' you should be careful if you're using self.raise_amount or
# Employee.raise_amount, because they COULD mean different things


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
        self.pay = int(self.pay) * self.raise_amount # note, must still refer to it by self! (can also be 
        # Employee.raise_amount, not necessarily self)
        print(self.pay)


print(Employee.num_of_emps) # prints out 0 because no new instances after new class declaration!