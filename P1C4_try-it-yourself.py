# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:45:01 2024

@author: nikumar
"""

# 4-1. Fruits: Think of at least three kinds of your favorite Fruit . Store these
# Fruit names in a list, and then use a for loop to print the name of each Fruit .
fruit_list = ['Mango', 'Lychee', 'Grapes', 'Blueberry']
for fruit in fruit_list:
    print(fruit.title())
# Modify your for loop to print a sentence using the name of the Fruit
# instead of printing just the name of the Fruit . For each Fruit you should
# have one line of output containing a simple statement like I like Fruit .
for fruit in fruit_list:
    print("I love", fruit.title(), "!!!!")

# Add a line at the end of your program, outside the for loop, that states
# how much you like Fruit . The output should consist of three or more lines
# about the kinds of Fruit you like and then an additional sentence, such as
# I really love Fruit!
for fruit in fruit_list:
    print("I love", fruit.title() + "!")
print("I like all kinds of fruits. Fruits are healthy!")

# 4-2. Animals: Think of at least three different animals that have a common char-
# acteristic . Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal .
pets_list = ['CAt', 'dog', 'ParroT']
for pet in pets_list:
    print(pet.title())

# Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# Add a line at the end of your program stating what these animals have in
# common . You could print a sentence such as Any of these animals would
# make a great pet!    
for pet in pets_list:
    print(pet.title())
print("All these pets are good for the house!")