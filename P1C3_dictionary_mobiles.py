# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:19:12 2024

@author: nikumar
"""

brands = ['apple', 'google', 'Xiaomi', 'samsung', 'Blackberry', 'Nothing']

print(brands)

# index starts at 0, not 1
## printing first element
print(brands[0])

## printing last element
print(brands[-1])

## string methods
print(brands[0].upper())
print(brands[-2].lower())

# IndexError: list index out of range
# we are trying to access the element which is not there
print(brands[10])
print(brands[-8])

# string concatenation
print("My first phone was " + brands[3].title() + " back in 2010.")
