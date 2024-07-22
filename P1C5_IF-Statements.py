# # -*- coding: utf-8 -*-
# """
# Created on Thu Jun 20 12:31:57 2024
# 
# @author: nikumar
# """
# # IF Condition
# bikes = ['tvs', 'royal Enfield', 'Ola', 'hero', 'Ather', 'ktm']
# 
# for bike in bikes:
#     if bike == 'tvs' or bike == 'ktm':
#         print(bike.upper())
#     else:
#         print(bike.title())
#         
# 
# age = 18
# age >= 18
# age < 18
# age == 18
# age <= 18
# 
# age_me = 38
# age_friend = 32
# 
# if age_me < 35 and age_friend < 35 :
#     print('both are less than 35')
# else:
#     print('someone is more than 35')
# 
# 
# # Checking Whether a Value Is in a List
# 'Ola' in bikes
# 'Bajaj' in bikes
# 
# # Checking Whether a Value Is Not in a List
# unsafe_countries = ['Pakistan', 'Bangladesh', 'Russia', 'Syria', 'Iraq']
# 
# user_wish = 'India'
# 
# if user_wish not in unsafe_countries:
#     print('You can travel to ', user_wish.title(), '. It is safe! ')
# else:
#     print('Please do not go to', user_wish.title())
#     
#     
# # if-else Statements
# print("Enter your age!")
# age = int(input())
# 
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry. You are not old enough to vote!")
#     print("Please register to vote as soon as you turn 18")
# print("Thank you for using this service!")
# 
# 
# # if - elif - else
# # consider an amusement park that charges different rates for different age groups:
# # Admission for anyone under age 4 is free.
# # Admission for anyone between the ages of 4 and 18 is $5.
# # Admission for anyone age 18 or older is $10.
# 
# # method 1
# 
# print("Welcome to the NS Amusement Park!. Please enter your age")
# age = int(input())
# if age <= 4:
#     print("Your admission fee is 0$")
# elif age >= 5 and age <= 17:
#     print("Your admission fee is 5$")
# else:
#     print("Your admission fee is 10$")
# 
# 
# # method 2
# 
# print("Welcome to the NS Amusement Park!. Please enter your age")
# age = int(input())
# price = 0
# if age <= 4:
#     price = 0
# elif age <= 18:
#     price = 5
# elif age > 65:
#     price = 5
# else:
#     price = 5
# 
# print("Your admission fee is " + str(price) + "$")
# 
# # second method is better since it avoids repetitive messages. 
# # to change the output statement, we can change once compared to thrice in method 1
# 
# 
# using if statements with lists
# 
# requested_flavours = ['vanilla', 'lychee', 'blueberry', 'pista', 'banana']
# 
# for topping in requested_flavours:
#     if topping == 'lychee':
#         print("sorry we are not having lychee flavour!")
#     else:
#         print("finished adding " + topping)

# Checking That a List Is Not Empty
# requested_flavours = []
# if requested_flavours:
#     for requested_flavour in requested_flavours:
#         print("finished adding " + requested_flavour + " flavour")
# else:
#     print("you have not selected any flavour. do you want a plain juice?")

# using multiple lists
available_flavours = ['mint', 'cola', 'lime', 'dry fruits', 'banana', 'chocolate']

requested_flavours = ['lime', 'cola', 'mango', 'chocolate']
print("Customer requested flavours: " + str(requested_flavours))
for requested_flavour in requested_flavours:
    if requested_flavour in available_flavours:
        print("Finished adding " + requested_flavour + ".")
    else:
        print("Sorry. We are out of "+ requested_flavour + "!")


