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

