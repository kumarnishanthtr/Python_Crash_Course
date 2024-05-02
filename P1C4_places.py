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


