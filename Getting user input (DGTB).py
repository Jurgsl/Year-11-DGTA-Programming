# Program: Getting user input
# Author: Juergen Lier
# Date: 26 June 2024
# Version 1

# TODO: Create and show variables
    # Ask a user for their name and store it in a variable
    # Greet the user

# Variables
# Constants are written in CAPITAL LETTERS. They don't change
HOURS_IN_DAY  = 24
PI = 3.14

# 'Normal' variables are written in lower case
number_in_class = 16
desk_nr = '8' # The number 8 is now a string, not a number.
chairs = '28'
greeting = 'Hello '
second_greeting = 'World'
num_1 = 8 # This variable contains a number
num_2 = 28

# We can add strings together. Its called concatenation
addition = desk_nr + chairs
print(addition)
addition = greeting + second_greeting
print(addition)

# Adding numbers together
addition = num_1 + num_2
print(addition)
multiply = num_1 * num_2
print(multiply)
divide = num_2/num_1
print(divide)

# Ask the user for their name and store it in a variable
name = input("What is your name? ")
print(f"Greetings to you earthling! I now know that your name is {name}")


