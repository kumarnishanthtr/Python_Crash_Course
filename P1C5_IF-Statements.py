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