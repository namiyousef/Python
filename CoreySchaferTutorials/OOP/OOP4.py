#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:32:05 2020

@author: yousefnami
"""

# SUBCLASSES

# video link: https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4

# Definitions:




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
        
        
class Developer(Employee): # inherits employee class properties
    pass


dev_1 = Developer('Yousef','Nami','5000')

print(dev_1.email)

# so what python does, is look for __init__ in developer, doens't find it, so goes to the parent 
# class looking for it


# when navigating things:

print(help(Developer))

# method resolution order: looks at Developer, then Employee, then builtins.object
# help(Developer) shows you what was inherited from where !

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
        
        
class Developer(Employee): # inherits employee class properties
    raise_amount = 1.10
    
emp_1 = Employee('Yousef','Nami',5000)
dev_1 = Developer('Mohammad','Nami',5000)

print(emp_1.pay)
emp_1.apply_raise()

print(dev_1.pay)
dev_1.apply_raise()


# made changes to the raise_amount without affecting that for the employees


# different instantiations 
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
        
        
class Developer(Employee): # inherits employee class properties
    raise_amount = 1.10
    
    def __init__(self,name,surname,pay,language):
        super().__init__(name,surname,pay) # this tells python to pass
        # name, surname and pay to the employee __init__ method, so tht it handles them
        # as opposed to repeating the code
        # ALTERNATE way of doing it: Employee.__init__(name,surname,pay)
        self.language = language
        
dev_1 = Developer('Yousef','Nami',5000,'Python')

print(dev_1.language)



# creating ANOTHER subclass 


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
        
        
class Developer(Employee): # inherits employee class properties
    raise_amount = 1.10
    
    def __init__(self,name,surname,pay,language):
        super().__init__(name,surname,pay) # this tells python to pass
        # name, surname and pay to the employee __init__ method, so tht it handles them
        # as opposed to repeating the code
        # ALTERNATE way of doing it: Employee.__init__(name,surname,pay)
        self.language = language
        
class Manager(Employee):
    raise_amount = 1.20
    
    def __init__(self,name,surname,pay,employees=None):
        super().__init__(name,surname,pay)
        if employees == None:
            self.employees = []
            # did not add empty list int he employee declaration employees = None
            # this is because tou don't wanna pass mutable objects in a declaration
        else:
            self.employees = employees
            
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def rem_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            emp.display_fullname()
            
            
mgr_1 = Manager('Yousef','Nami',9000,[dev_1])

print(mgr_1.email)
mgr_1.print_emps()

                     