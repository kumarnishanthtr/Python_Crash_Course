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


# 5.8 Hello Admin: Make a list of five or more usernames, including the name
# 'admin' . Imagine you are writing code that will print a greeting to each user
# after they log in to a website . Loop through the list, and print a greeting to
# each user:

# If the username is 'admin', print a special greeting, such as Hello admin,
#would you like to see a status report?

# Otherwise, print a generic greeting, such as Hello Eric, thank you for log-
# ging in again.

#user_list = ['furiousfrodo', 'admin', 'sweet1214', 'admin', 'nimittha']

for user in user_list:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+ user + "!, Thank you for logging in!")
        

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty .
# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct
# message is printed
user_list = []

if user_list:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+ user + "!, Thank you for logging in!")
else:
    print("We need to find some users!")


# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username .
# Make a list of five or more usernames called current_users .
# Make another list of five usernames called new_users . Make sure one or
# two of the new usernames are also in the current_users list .
# Loop through the new_users list to see if each new username has already
# been used . If it has, print a message that the person will need to enter a
# new username . If a username has not been used, print a message saying
# that the username is available .
# Make sure your comparison is case insensitive . If 'John' has been used,
# 'JOHN' should not be accepted .

current_users = ['john', 'spex', 'zuck', 'nish', 'swa']
new_users = ['nimi', 'NISH', 'swathi', 'max', 'John']
[x.lower() for x in current_users] # list comprehension
for user in new_users:
    
    if user.lower() in current_users:
        print (user + ": Sorry that username is taken")
    else:
        print(user + ": Username is available!")
        

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd . Most ordinal numbers end in th, except 1, 2, and 3 .
# Store the numbers 1 through 9 in a list .
# Loop through the list .
# Use an if-elif-else chain inside the loop to print the proper ordinal end-
# ing for each number . Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line .

numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print('1st \n')
    elif number == 2:
        print('2nd \n')
    elif number == 3:
        print('3rd \n')
    else:
        print(str(number) + 'th \n')
        