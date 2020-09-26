# getters, setters and deleters

# video: https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6&ab_channel=CoreySchafer

# Definitions:


class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property #defines a method like an attribute, so now, you can refer to instance.email instead of
    #instance.email() and it will refer to it as the return of email function
    def email(self):
        return '{}.{}@hotmail.com'.format(self.first,self.last)
    
    @fullname.setter
    def fullname(self, name): #name is the value that we are trying to set
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None 
        self.last = None
        
    # so now, the fullname setter class can behave in two ways:
    # either as an attrivute creator, so 
        """
        instance = Employee('first','last')
        print(instnace.fullname) # not sure if need to put employee()? 
        # this will print 'first last' since it already exists as an attribute (even though it's a method)
        """
    # OR as a device that updates other attributes:
        """
        instance = Employee('first','last')
        instance.employee = 'Yousef Nami'
        # will update self.first and self.last to Yousef, Nami respectively
        """
    # OR as a deleter
        """
        instance = Employee('first','last')
        del instance.fullname # will delete first.last, first.first 
        # WILL is also delete the first.fullname?
        """
emp_1 = Employee('Django','Unchained')
#emp_1.first = 'Jim'


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# NOTE: email still has django, because it is based on the initial instantiation of the class, any modiciations
# did not update that instantiation.



