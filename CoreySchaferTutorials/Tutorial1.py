#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:07:20 2020

@author: yousefnami
"""

# youtube link: https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2

message = 'Yousef\'s Toy' #using \' allows you to write ' in text
message = "Yousef\"s toy" #like above
#alternatively, you can use double / single quotes when you have single / double quotes in text respectively
message = 'yousef"s toy'
message = "yousef's you"

print(message)

test1 = 'test'
test2 = "test"

print(len(test1))
print(len(test2))

# as you can see, a string is always characters! Double or single brackets don't change this!
#when you refer to an array, so for example message[0:5], you're NOT including the 5, but you're including the 0!!

#example:
list1=[1,2,3,4]
print(list1[0:4])

#if you do: list1[0:] then it's the same as list1(0:end) in matlab !

test = "YeSs"
print(test.lower()) #turns the case to lower case
print(test.upper()) #turns the text to upper
print(test.count('s')) #counts the occurance of 's'
print(test.find('s')) #finds index of the letter 's' when it first appears
#if it can't find it, then it turns negative 1

print(test.replace("S",'s'))

#useful text editing skill!!!!!

Name = 'Yousef'
message = "Hi, my name is {}".format(Name) #this is very useful for a for loop I presume
print(message)

# alternative method to above!
message = f"Hi, my name is {Name}"
print(message)

#these string types are powerful, because u can do some extra text editing!

#for exampel:

message = f'Hi, my name is {Name.upper()}'
print(message)

#much like JS, you can also compound functions. So for example: line 46, you could add .format(Name).upper() do achieve the same tihng!


#use 'dir()' to get functions thar yoiu can use.

print(dir(Name)) #gives you all the functions that you can apply to a string type (Name)

#there's also:
print(help(str))
#can also do:
print(help(str.lower))