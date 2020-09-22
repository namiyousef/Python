#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:17:34 2020

@author: yousefnami
"""

#importing modules

import Tutorial9_functions as test #imports the custom file we made as 'test'

courses = ['Maths','Physics','Engineering']
course = 'MechEng'

course_2 = test.finder(course,courses)
print(course_2) 

#alternatiely, you could just import a single function
from Tutorial9_functions import finder #you can import more than one thing at a time
#for example you can say:
"""
from Tutorial9_functions import finder, function2, funtion3
"""
#alternatively, can also import 'everything'
"""
from Tutorial9_function import *
"""
#the above is dangerous though, because u lose track of what has been imported and what hasn't been

courses = ['Maths','Physics','Engineering']
course = 'MechEng'

course_2 = finder(course,courses) #as you can see, you don't need test., you can refer to the fucntion directly
print(course_2) 


#the import function checks for what you are importing within sys.path (i.e. the directory you are in and other things)

#look below:
import sys #need to import sys to show path!
print(sys.path) #these are all the places that python looks for to find functions that you are trying to import

#for a link to see how all o this stuff works: https://www.youtube.com/watch?v=CqvZ3vGoGs0

#if you have a file stored on a custom location, then you can simply append that location to sys.path so that
#python look at it
#example: sys.path.append('t')


#you can change the python 'environment' as well, instead of doing it like you are trying to above. 
#in terminal, write: nano ~/.bash_profile
#then: export PYTHONPATH="the location of the custom directly that you are saving your files in"
#this then permanently adds the path to that directory to your python default path
#you might have to do something similar for "Spyder", check this online: "search: spyder python path"