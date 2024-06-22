# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:31:57 2024

@author: nikumar
"""
# IF Condition
bikes = ['tvs', 'royal Enfield', 'Ola', 'hero', 'Ather', 'ktm']

for bike in bikes:
    if bike == 'tvs' or bike == 'ktm':
        print(bike.upper())
    else:
        print(bike.title())
        

age = 18
age >= 18
age < 18
age == 18
age <= 18

age_me = 38
age_friend = 32

if age_me < 35 and age_friend < 35 :
    print('both are less than 35')
else:
    print('someone is more than 35')


# Checking Whether a Value Is in a List
'Ola' in bikes
'Bajaj' in bikes

# Checking Whether a Value Is Not in a List
unsafe_countries = ['Pakistan', 'Bangladesh', 'Russia', 'Syria', 'Iraq']

user_wish = 'India'

if user_wish not in unsafe_countries:
    print('You can travel to ', user_wish.title(), '. It is safe! ')
else:
    print('Please do not go to', user_wish.title())
    
    
# if-else Statements
print("Enter your age!")
age = int(input())

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry. You are not old enough to vote!")
    print("Please register to vote as soon as you turn 18")
print("Thank you for using this service!")


# if - elif - else
# consider an amusement park that charges different rates for different age groups:
# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $5.
# Admission for anyone age 18 or older is $10.
print("Welcome to the NS Amusement Park!. Please enter your age")
age = int(input())
if age <= 4:
    print("Your admission fee is 0$")
elif age >= 5 and age <= 17:
    print("Your admission fee is 5$")
else:
    print("Your admission fee is 10$")