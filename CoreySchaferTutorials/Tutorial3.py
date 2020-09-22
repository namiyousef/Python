#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:44:47 2020

@author: yousefnami
"""

#lists, tuples and sets

courses = ['history','math','compsci']

#can use negative indexes, which basically starts from the otherside
#so:
print(courses[-1])

#list methods

#append adds smth a tthe back of the course
#so:
courses.append('art')
print(courses)

courses.insert(0,'art2') #first thing it takes is the index wherre you want 'art2' added
print(courses)

#note that you can make a mistake to have a list within a list, an example of this is shown below:
List2= [[1,2,3],4,5]
print(List2)
print(List2[0][0])
print(List2[0])

#so that's why, if you wanna combine lists, then you need to do 'extend'
#so:
list3=[1,2]
courses.extend(list3)
print(courses)
print(courses[-1]+2) #as you can see list values can take differnet data types!

#note that for the above, using insrt or append would add a list withint eh list, but not the values of that list!

#remove values!

courses.remove('math')
print(courses)

courses.pop() #removes the last value, and returns it
#so:
test = courses.pop()
print(test)

courses.reverse() #reverses list

courses.sort() #only works if you have strings / numbers! #sorts in ascending for numbers and alphabetical for letters
print(courses)


test = [1,2,3,'c','d','f']

#can also do:

g = [1,4,5,73,2,6,743,3]
print(g)
g.sort(reverse = True )
print(g)


#to set a variable, then we use: "sorted"
#so:

list4=[1,3,54,6,3,7,3]
#if you use list4.sort(), then tou'll alter the original list
#but if you use sorted, then you can save it as a new var
list4_sorted = sorted(list4)
print(list4,list4_sorted)


#can also use, min, max and sum!

#to find the index of a value by 'searching'
print(list4.index(1))

#you can check if there's a value in a list, for exampl:
list_1 = ['Math']
list_2 = ['math']
print('Math' in list_1)
print('Math' in list_2)

#tip for for looping!!!!
courses = ['CCM','ECM']
for index, course in enumerate(courses): #loops through courses and makes note of the index as well, this is achieved by using the enumerate() method
    print(index, course)

#can also change the 'start' point of the index
for index, course in enumerate(courses, start = 1):
    print(index, course)
    #the above is useful if say, you wanna count smth for the sake of counting 


# can change a list to nicely laid out comma separated values using 'join'

course_str = ', '.join(courses)
print(course_str)

#can also split a string:
list_new = course_str.split(', ')
print(list_new)




""" tuples and sets"""

#tuples cannot be modified
courses = ['Maths','CCM']
courses2 = courses
courses[0] = 'Art'
print(courses,courses2) #wtf this is so weird....
#to copy a list properly
courses2 = courses.copy()
courses[0]='Maths'
print(courses,courses2)

tuple1 = ('Maths','CCM') #round brackets used. This cannot be changed!

#uncomment the following line (it will give u an error!)

#tuple1[0]= 'Art' #it will not change!

set_1 = {'Maths','Art','Test','Tujhaz'} #does not care about order
#so:
print(set_1) #the output is not the same as the input
#sets are used to check for duplicates, for example:

set_1 = {1,2,3,2,4,1,1}
print(set_1)

#another example:

set_1 = {'Maths','Art','Test','tuweiw','wjjdejd'}
set_2 = {'Maths','Art','Test','Tujhaz'}
#if you wanna find the common courses:
print(set_1.intersection(set_2))
#or:
print(set_1.difference(set_2)) #shows courses thst are in set 1 but not in2
#can also combine them: 
print(set_1.union(set_2))


#to create empty tuples, sets or lists

list1= []
#or
list1 =list()


tuple1 =()
#or 
tuple1 = tuple()


set1={} #this creates a dictionary, NOT a set

set1 = set()