# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:25:47 2024

@author: nikumar
"""

# modifying elements in the list
phones = ['nokia', 'samsung', 'nothing', 'apple']
print(phones)

# modify nokia to google
phones[0] = 'google'
print(phones)

# modify apple to oneplus
phones[-1] = 'oneplus'
print(phones)

# adding new elements to the list
# using `append` (new elements added at the end)
phones.append('oppo')

# using `insert` (new elements at any position)
phones.insert(0, 'vivo')
phones.insert(-1, 'realme')
print(phones)
