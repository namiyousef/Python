# Video link: https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=5&ab_channel=CoreySchafer

# SPECIAL METHODS (magic methods)

# Definitions:
# Dunder: refers to objects sandwiched between __, so dunder init --> __init__
# __repr__: unambiguious representation of the object
# __str__: user-friendly readable represenation of the object


print(1+2)
print('a'+'b')

# the + operator does different things for different objects


# the above are important special methods! 

class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self,name,surname,pay):
        self.name = name 
        self.surname = surname 
        self.email = '{}.{}@hotmail.com'.format(name,surname)
        self.pay = pay
        Employee.num_of_emps += 1 # adds 1 each time a new class is instantiated! 
    
    def __repr__(self): # note, if you don't have __repr__, then __str__ will just refer to __repr__
        return "Employee('{}','{}',{})".format(self.name,self.surname, self.pay)
    
    def __str__(self):
        return "{} - {}".format(self.display_fullname(),self.email)    
    
    def display_fullname(self):
        return '{} {}'.format(self.name,self.surname)
        
    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount
        print(self.pay)
        
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.display_fullname())
        
        
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
            
    def __repr__(self):
        return "Manager('{}','{}',{})".format(self.name,self.surname, self.pay)
    
    
          
emp_1 = Employee('Yousef','Nami','5000')
mgr_1 = Manager('Mohd','Nami','10000')
print(emp_1)
print(mgr_1)

# returns the instantiations of the elements! 
# when you print(objet) then you can change how your object is shown!

print(emp_1.__repr__())
print(emp_1.__str__())


print(str.__add__('a','b'))
print(int.__add__(1,2))


print(emp_1 + mgr_1) # wow! This is smart eh?


print(len('test'))
print('test'.__len__())


print(len(emp_1))

# essentially, you can cut down a lot of code by using 'standard' methods. 
# so for example, suppose that you have a numpy array, and you want to find it's length using the 
# len function, then you can add a special method inside your class that does that conversion for u

# you can 'return NotImplemented' if something does not work the way you want it to, whch allows you 
# instead of breaking code, to allow a fallback to a previous object
