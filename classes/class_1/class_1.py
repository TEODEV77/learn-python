# This script explains how to create and use string variables in Python.

# Creating a string variable
# A string is a sequence of characters enclosed in quotes. You can use single quotes (' ') or double quotes (" ").
greeting = "Hello, World!"  # This is a string variable using double quotes.
name = 'TEODEV77'  # This is a string variable using single quotes.

# Printing string variables
# The print() function outputs the specified message to the console.
print(greeting)  # Output: Hello, World!
print(name)  # Output: TEODEV77

# Concatenating strings
# You can concatenate (join) two or more strings using the + operator.
full_greeting = greeting + " My name is " + name + "."
print(full_greeting)  # Output: Hello, World! My name is TEODEV77.

# Using f-strings (formatted strings)
# An f-string allows you to embed expressions inside string literals using curly braces {}.
age = 27
introduction = f"My name is {name} and I am {age} years old."
print(introduction)  # Output: My name is TEODEV77 and I am 27 years old.

# Requesting user input
# The input() function prompts the user for input and returns it as a string.
# The prompt string is displayed to the user.
user_name = input("Enter your name: ")  # Prompts the user to enter their name.
user_age = input("Enter your age: ")  # Prompts the user to enter their age.

