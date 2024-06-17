# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:34:29 2024

@author: nikumar
"""

# 4 WORKING WITH LISTS

# for Loop
# list of places I've been to
import random
from datetime import date
places_visted = ['Goa', 'Dehradun', 'Mumbai', 'Pondicherry', 'Delhi', 'Hyderabad', 'Munnar', 'Mysore', 'Udupi']
year = 2000
for place in places_visted:
    print('year:', year)
    print(place.lower(), 'was a great place!')
    print("I can't wait to travel again", "\n")
    year = year + random.randint(1, 5)
# “For every place visited in the list of places, print the place name.”
print("All in all, it was good life!")

# indentation error
for place in places_visted:
print(place)
# IndentationError: expected an indented block after 'for' statement on line 1


# line 33 should be indented but it is not. No error but not expected output. 
# this is Logical Error
for place in places_visted:
    print(place.title(), "was great!")
print("can't wait to go back to", place.upper(), "again!")    


# unexpected indent
message = "Today is " +  str(date.today())
    print(message)
    

# indenting unnecessarily after the loop
print("Lets print the places I visited...")
for place in places_visted:
    print(place.title())
    print("...Loop Ends")

# Logical Error on line 46. It has unexpected indent which makes it run it inside loop.

# Dont forget the colon!
for place in places_visted
    print(place.title())

"""
Created on Tue May 28 11:23:51 2024

@author: nikumar
"""

# Making numerical lists
# using range() function
for value in range(1,6):
    print(value)

# it never prints 6 because it stops at 6 and doesn't print it.

# Using range() to Make a List of Numbers
numbers = list(range(1,6))
    

# making a list of even numbers using range()
even_num = list(range(0, 10, 2))
print(even_num)

# making a list of odd numbers using range()
odd_num = list(range(1, 10, 2))
print(odd_num)


# creating a range of squared numbers from 1 to 10
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# simple math functions
numbers = list(range(0,11))


min(numbers)
max(numbers)
sum(numbers)

# List Comprehensions
squares_new = [value**2 for value in range(1,11)]
print(squares_new)

# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:28:07 2024

@author: nikumar
"""
os_names = ['android', 'ios', 'linux', 'windows', 'symbian']

# Slicing a List 
print(os_names[0:3])

# and 

print(os_names[:3])

# are same. 0 is automatically added if starting range is not specified.

# similarly

print(os_names[2:5])

# and

print(os_names[2:])

# are same. 

# also negative index returns that many elements from the end

print(os_names[-1:])

# this prints the last element. this is useful when we don't know the length of the list

# Looping Through a Slice

cities = ['Masthikatte', 'Gundlupet', 'Shimoga', 'Bangalore']

print("Here are the first two cities i studied school...")
for city in cities[:2]:
    print(city.title())
    

# Copying a List
my_foods = ['Pizza', 'Vada Pav', 'Heerekaayi Dosa', 'Pulav']

friend_foods = my_foods[:]


copy_foods = my_foods
#In this case, copy_foods is not a new list. Instead, it is a reference to the same list object that my_foods refers to.
# Any changes made to copy_foods will also affect my_foods because they both point to the same list object. They are two references to the same data.

copy_foods.append('Ice cream')
copy_foods.remove('Pulav')

my_foods.append('Pav Bhaji')
friend_foods.append('Burger')


# Tuples
# Python refers to values that cannot change as immutable, 
# and an immutable list is called a tuple.


dimensions_list = [200, 50] # list
dimensions_tuple = (200, 50) #tuple

# try to change the first value from 200 to 300
dimensions_list[0] = 300 # success!
dimensions_tuple[0] = 300 # TypeError: 'tuple' object does not support item assignment

# Writing over a Tuple
# Although you can’t modify a tuple, 
# you can assign a new value to a variable that holds a tuple.
dimensions_tuple = [300, 50] # assign new values to variable instead of changing specific element


# Styling your Code
# Python Enhancement Proposal (PEP). One of the oldest PEPs is PEP 8
# PEP 8 recommends that you use four spaces per indentation level.
for x in x_list:
    print(x)
    if x > 100:
        print('greater')
    else:
        print('lower')
        
# PEP recommend that each line should be less than 80 characters.
# PEP 8 also recommends that you limit all of your comments to 72 characters per line
# Comments that contradict the code are worse than no comments. 
# Always make a priority of keeping the comments up-to-date when the code changes!
# To group parts of your program visually, use blank lines.
   