# Python_Crash_Course
My Python Playground: A solo journey through 'Python Crash Course' by Eric Matthes. Each file is a chapter conquered, a step in my coding evolution. No frills, just me, the code, and the quest to master Python.

## Table of Contents
- [Chapter 1: Getting Started](#chapter-1-getting-started)
- [Chapter 2: Variables and Simple Data Types](#chapter-2-variables-and-simple-data-types)


## Chapter 1: Getting Started
In this chapter we found out about the different versions of Python available. And helpful guides on downloading and installing Python for Windows/Linux and Mac OS. We also learnt how to write a simple program to display a print statement. 

### Key Concepts
- **Python versions:** Currently, there are two types of Python available to download. Python2 and Python3

### Code Snippets
```python
# Simple program to display a message using print statement
print("Hello, World!")
```

## Chapter 2: Variables and Simple Data Types
Variable holds a value. Python keeps track of its current value. Variables cannot start with a number ex: `1_variable`, Variables cannot have spaces ex: `my message`. Avoid using function names as variables ex: `print`. Variable names should be short and description. ex: `name_length` and not `n_l` or `length_of_the_name`. 
We have many datatypes. Strings, used for storing charaters. There are many methods on strings such as making them upper, lower and proper case. We also learnt how to join two or more strings, adding a tab space to the string, making the string appear in new line  to create a friendly greeting message and we also learnt how to clean up the data by removing whitespaces

### Key Words
- **NameError:** means we either forgot to set a variable’s value before using it, or we made a spelling mistake when entering the variable’s name.
- **Strings:** Anything inside a single/double quote is a string. These are a type of datatype which is used to store a series of characters.
- **Methods:** A method is an action that Python can perform on a piece of data.
- **Concatenation:** Method of combining strings
- **Whitespace:** Any nonprinting character, such as spaces, tabs, and end-of-line symbols.

### Code Snippets
```python
# Computers are strict, but they disregard good and bad spelling.
mesage = "Hello Python Crash Course reader!"
print(mesage)

# methods for string
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```

