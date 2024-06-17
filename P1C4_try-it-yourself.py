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

# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:04:17 2024

@author: nikumar
"""

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive .
for number in range(1, 21):
    print(number)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers . (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window .)
million = list(range(1, 1000001))
for value in million:
    print(value)

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million . Also, use the sum() function to see how quickly Python can
# add a million numbers .
min(million)
max(million)
sum(million)

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20 . Use a for loop to print each number .
odd_numbers = list(range(1,10,2))
print(odd_numbers)


# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30 . Use a for loop to
# print the numbers in your list .
threes = list(range(3,31,3))
for three in threes:
    print(three)


# 4-8. Cubes: A number raised to the third power is called a cube . For example,
# the cube of 2 is written as 2**3 in Python . Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube .
numbers = list(range(1,11))
cubes = []
for value in numbers:
    cube = value ** 3
    cubes.append(cube)

print(cubes)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes .
cubes_new = [value ** 3 for value in range(1,11)]
print(cubes_new)

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# 1.Print the message, The first three items in the list are: . Then use a slice to
#   print the first three items from that program’s list .
# 2.Print the message, Three items from the middle of the list are: . Use a slice
#   to print three items from the middle of the list .
# 3. Print the message, The last three items in the list are: . Use a slice to print
#    the last three items in the list
fruit_list = ['Mango', 'Lychee', 'Grapes', 'Blueberry', 'Papaya', 'Pineapple', 'Orange', 'Banana']
print('The first three items in the list are:')
print(fruit_list[:3])

print('Three items from the middle of the list are')
print(fruit_list[3:6])

print('The last three items in the list are')
print(fruit_list[-3:])

# 4-11. Start with your program from Exercise 4-1
# (page 60) . Make a copy of the list of dosa, and call it friend_dosa .
my_dosa = ['Masala', 'Onion', 'Set', 'Heerekaayi']
friend_dosa = my_dosa[:]

# Then, do the following:

# 1. Add a new dosa to the original list .
my_dosa.append('Tomato')

# 2. Add a different dosa to the list friend_dosa 
friend_dosa.append('Pineapple') # eww

# 3. Prove that you have two separate lists . Print the message, My favorite
#   dosa are:, and then use a for loop to print the first list . Print the message,
#   My friend’s favorite dosa are:, and then use a for loop to print the sec-
#   ond list . Make sure each new dosa is stored in the appropriate list .    
print('My favourite dosa are:')
for i in my_dosa:
    print(i.title())

print('My friend’s favourite dosa are:')
for i in friend_dosa:
    print(i.title())

# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space . Choose a version of foods.py, and
# write two for loops to print each list of foods 
print("Different varieties of Dosa I like!")
for dosa in my_dosa:
    
    print(dosa.title() + ' Dosa')

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods . Think of five
# simple foods, and store them in a tuple .
NSCafe_Menu = ('Broost', 'Lemon Grass Shtea', 'Leminty', 'Chashayam')

# 1 Use a for loop to print each food the restaurant offers .
for food in NSCafe_Menu:
    print(food.title())
    
# 2 Try to modify one of the items, and make sure that Python rejects the change .
NSCafe_Menu[0] = 'Bouramman Vita'
# TypeError: 'tuple' object does not support item assignment

# 3 The restaurant changes its menu, replacing two of the items with different foods.
# Add a block of code that rewrites the tuple, 
# and then use a for loop to print each of the items on the revised menu .
NSCafe_Menu = ('Bouramman Vita', 'Dicapi', 'Leminty', 'Chashayam')
for food in NSCafe_Menu:
    print(food.title())
    
# 4-14. PEP 8: Look through the original PEP 8 style guide 
# at https://python.org/ dev/peps/pep-0008/ . 
# You won’t use much of it now, but it might be interesting to skim through it .    

# 4-15. Code Review: Choose three of the programs you’ve written in this chapter
# and modify each one to comply with PEP 8:

# 1. Use four spaces for each indentation level . Set your text editor to insert
#    four spaces every time you press tab, if you haven’t already done so (see
#    Appendix B for instructions on how to do this) .
from random import randrange
x = randrange(10)
if x < 5:
    print(str(x) + ' is less than 5')
elif x <= 10:
    print(str(x) + ' is between 5 and 10')

# 2. Use less than 80 characters on each line, and set your editor to show a
#    vertical guideline at the 80th character position .

# Don’t use blank lines excessively in your program files .
# OK MATE!