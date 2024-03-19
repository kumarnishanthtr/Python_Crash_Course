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

# Changing, adding, and removing elements
favourites[0] = 'TVS' # modified first element as TVS

# adding element to a list
# using Append (adding at the end)
favourites.append('Pulsar')
print(favourites)

tvshow_list = []
tvshow_list.append('Game of Thrones')
tvshow_list.append('Breaking Bad')
tvshow_list.append('Two and a Half Men')
tvshow_list.append('The Simpsons')

# using Insert (adding by specifying position)
tvshow_list.insert(0, 'Silli Lalli') # 0 is the index. This shifts the other elements to the right
tvshow_list.insert(-1, 'Full House') # this does not add to the last but adds at the one before last. 

# removing elements
# using del
del favourites[-1] # this removes pulsar 

# using pop
states_travelled = ['MH', 'GA', 'UK', 'TN', 'KL', 'AP']

pop_state = states_travelled.pop()
print(states_travelled)
print(pop_state)

# using pop, specify the index to remove the element
states_travelled = ['MH', 'GA', 'UK', 'TN', 'KL', 'AP']
north_india = states_travelled.pop(2)
print(north_india)

# using pop, by default it removes the last element in the list and returns the value unlike del
states_travelled = ['MH', 'GA', 'UK', 'TN', 'KL', 'AP']
states_travelled.pop() # removes and returns 'AP'
del states_travelled[-1] # removes 'AP' but does not return


# removing an Item by Value
# remove
asian_countries = ['india', 'china', 'japan', 'indonesia', 'finland', 'sri lanka']

# we need to remove 'finland' value
asian_countries.remove('finland')

asian_countries = ['india', 'china', 'japan', 'indonesia', 'finland', 'sri lanka']
not_asia = 'finland'
asian_countries.remove(not_asia)
print(not_asia.title() + ' is not in Asia!')


