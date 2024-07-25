# Chapter 6 :DICTIONARIES

# example
# this is a dictionary of a type of alien in a game. different alien has different characteristic

alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['points'])
# print(alien_0['color'])

# working with dictionaries
# A dictionary in Python is a collection of key-value pairs.
# Each key is connected to a value
# Key's value can be a number/string/list/dict
simple_dic = {'country': 'india'}

# Accessing Values in a Dictionary
print(simple_dic['country'])

# Adding New Key-Value Pairs
# Dictionaries are dynamic structures, and you can add new key-value pairs
# to a dictionary at any time.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# add new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Python doesn’t care about the order in which you store each key-value pair;
# it cares only about the connection between each key and its value.

# Starting with an Empty Dictionary
alien_0 = {}

alien_0['color'] = 'red'
alien_0['points'] = 20
alien_0['difficulty'] = 'easy'
print(alien_0)

# Modifying Values in a Dictionary

alien_0 = {'color': 'yellow'}
print("The alien color is " + alien_0['color'] + '.')

alien_0['color'] = 'red'
print("The alien color is now " + alien_0['color'] + ".")

modify the value based on condition
alien_0 = {'x_position' : 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

Move the alien to the right.
Determine how far to move the alien based on it's current speed.

if alien_0['speed'] == 'low':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

print("The current x-position of alien is: " + str(alien_0['x_position'] + x_increment))

# Removing Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# Be aware that the deleted key-value pair is removed permanently