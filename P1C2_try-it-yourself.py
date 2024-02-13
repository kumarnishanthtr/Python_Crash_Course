# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:30:53 2024

@author: nikumar
"""

# 2-3. Personal Message: Store a person’s name in a variable, and print a message
# to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

person_name = 'Eric'
print('Hello '+ person_name + ', would you like to learn some Python today?')

# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s
# name in lowercase, uppercase, and titlecase.
person_name = 'Eric Cartman'
print(person_name.title())
print(person_name.lower())
print(person_name.upper())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# “I wish it need not have happened in my time," said Frodo.
# "So do I," said Gandalf, "and so do all who live to see such times. But that is not for them to decide. All we have to decide is what to do with the time that is given us.”
# ― J.R.R. Tolkien, The Fellowship of the Ring
famous_quote = '“I wish it need not have happened in my time," said Frodo.' + '"So do I," said Gandalf, "and so do all who live to see such times. But that is not for them to decide. All we have to decide is what to do with the time that is given us.”' + '\n ― J.R.R. Tolkien, The Fellowship of the Ring'
print(famous_quote)

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s
# name in a variable called famous_person. Then compose your message
# and store it in a new variable called message. Print your message.
famous_person = 'J.R.R. Tolkien'
print('“I wish it need not have happened in my time," said Frodo.' + '"So do I," said Gandalf, "and so do all who live to see such times. But that is not for them to decide. All we have to decide is what to do with the time that is given us.”' + '\n - ' + famous_person + ', The Fellowship of the Ring')


# 2-7. Stripping Names: Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip(). 

person_name = '\t   Danny Tanner   \n'
print(person_name)

print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())

person_name = person_name.lstrip()
person_name = person_name.rstrip()
person_name = person_name.strip()

print(person_name)

# 2-8. Number Eight: Write addition, subtraction, multiplication, and division
# operations that each result in the number 8. Be sure to enclose your operations
# in print statements to see the results. You should create four lines that look
# like this:
# print(5 + 3)
# Your output should simply be four lines with the number 8 appearing once
# on each line.

print(4 + 3 + 1)
print(100 - 92)
print((3 * 2) + 2)
print(40 / 5)


# 2-9. Favorite Number: Store your favorite number in a variable. Then, using
# that variable, create a message that reveals your favorite number. Print that
# message.
favourite_num = 14
print('My favorite number is ' + str(favourite_num))


# 2-10. Adding Comments: Choose two of the programs you’ve written, and
# add at least one comment to each. If you don’t have anything specific to write
# because your programs are too simple at this point, just add your name and
# the current date at the top of each program file. Then write one sentence
# describing what the program does.
# comment to print the quote
print("\t'Not all who wanders are lost' \n\t - J.R.R Tolkien")

# 2-11. Zen of Python: Enter import this into a Python terminal session and skim
# through the additional principles
import this
