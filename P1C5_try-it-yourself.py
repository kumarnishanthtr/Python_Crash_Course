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
