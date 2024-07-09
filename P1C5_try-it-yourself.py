# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:21:20 2024

@author: nikumar
"""

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\nIs car != 'Mercedes'? I predict True")
print(car!= 'Mercedes')
print("\nIs car != 'subaru'? I predict False")
print(car!= 'subaru')

print("\nIs car.upper() == 'subaru'? I predict False")
print(car.upper() == 'subaru')
print("\nIs car.upper() == 'SUBARU'? I predict False")
print(car.upper() == 'SUBARU')
print("\nIs len(car) == 6? I predict True")
print(len(car) == 6)
print("\nIs len(car) > 8? I predict False")
print(len(car) > 8)
print("\nIs len(car) >= 6? I predict True")
print(len(car) >= 6)
print("\nIs len(car) <= 1? I predict True")
print(len(car) <= 10)
print("\nIs len(car) <= 6? I predict True")
print(len(car) <= 6)

age = 10
print("age = 10")
print('\nIs age >= 5 and age <= 15? I predict True')
print(age >= 5 and age <= 15)
print('\nIs age >= 15 or age <= 15? I predict True')
print(age >= 15 or age <= 15)

capital_cities = ['Mumbai', 'Bengaluru', 'Kolkata', 'Chennai']
print(capital_cities)
print('\nIs Pune in capital_cities? I predict False')
print('Pune' in capital_cities)

numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers)
print('\nIs 6 in numbers? I predict True')
print(0 in numbers)

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game . Create a
#variable called alien_color and assign it a value of 'green', 'yellow', or 'red' .
alien_color = 'red'
# 1. Write an if statement to test whether the alien’s color is green . If it is, print
# a message that the player just earned 5 points .
if alien_color == 'green':
    print("you have earned 5 points!")
    
# 2. Write one version of this program that passes the if test and another that
# fails . (The version that fails will have no output .)

# pass
alien_color = 'green'
if alien_color == 'green':
    print("you have earned 5 points!")

# fail
alien_color = 'red'
if alien_color == 'green':
    print("you have earned 5 points!")

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain .
alien_color = 'red'
# 1. If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien .
if alien_color == 'green':
    print('you have earned 5 points!')


# 2. If the alien’s color isn’t green, print a statement that the player just earned
# 10 points .
if alien_color != 'green':
    print('you have earned 10 points!')

# 3. Write one version of this program that runs the if block and another that
# runs the else block .
if alien_color == 'green':
    print('you have earned 5 points!')
else:
    print('you have earned 10 points!')
    

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-
# else chain .

# If the alien is green, print a message that the player earned 5 points .
# If the alien is yellow, print a message that the player earned 10 points .
# If the alien is red, print a message that the player earned 15 points .

# Write three versions of this program, making sure each message is printed
# for the appropriate color alien .

alien_color = 'red'

if alien_color == 'green':
    print('you have earned 5 points!')
elif alien_color == 'yellow':
    print('you vae earned 10 points!')
else:
    print('you have earned 15 points!')
    
    
# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life . Set a value for the variable age, and then:
# If the person is less than 2 years old, print a message that the person is
# a baby .
# If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler .
# If the person is at least 4 years old but less than 13, print a message that
# the person is a kid .
# If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager .
# If the person is at least 20 years old but less than 65, print a message that
# the person is an adult .
# If the person is age 65 or older, print a message that the person is an
# elder .

age = 34
if age <= 2:
    print('you are a baby')
elif age <= 4:
    print('you are a toddler')
elif age <= 13:
    print('you are a kid')
elif age <= 20:
    print('you are a teenager')
elif age <= 65:
    print('you are a adult')
else:
    print("you are a elder")
    
    
# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list .
# Make a list of your three favorite fruits and call it favorite_fruits .
# Write five if statements . Each should check whether a certain kind of fruit
# is in your list . If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!

favourite_fruits = ['lychee', 'mango', 'blueberry']

if 'banana' in favourite_fruits:
    print("you really like banana")

if 'lychee' in favourite_fruits:
    print("you really like lychee")


if 'jackfruit' in favourite_fruits:
    print("you really like jackfruit")


if 'blueberry' in favourite_fruits:
    print("you really like blueberry")


if 'papaya' in favourite_fruits:
    print("you really like papaya")
