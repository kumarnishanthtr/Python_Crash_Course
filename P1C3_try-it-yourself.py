# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:49:48 2024

@author: nikumar
"""

# 3-1. Names: Store the names of a few of your friends in a list called names . Print
# each person’s name by accessing each element in the list, one at a time .
names = ['Gunda', 'Avi', 'Devadatta', 'Pratheek', 'Nitish', 'Shreyamsha']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-2])
print(names[-1])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them . The text of each mes-
# sage should be the same, but each message should be personalized with the
# person’s name .

message = "Hey there, "
print(message + names[0])
print(message + names[-2])


# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples . Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle .”
favourites = ['BMW', 'Triumph', 'Kawasaki', 'RE Himalayan']
print('I love riding a ' + favourites[1] + ' bike in a forest trail')
