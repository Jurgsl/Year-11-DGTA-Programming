# Program: Getting user input
# Author: Juergen Lier
# Date: 25 June 2024
# Version 1

# TODO: Ask for user input (Their name)
        # Store that name
        # Greet the user with the stored name
        # Ask for two numbers
        # Multiply and add them together
        # Display the results to the user

# Ask the user for their name
name = input("Good day, what is your name? \n")

# Greet the user and ask for their favourite numbers (x2) and store them
# print("Hi", name,". Please answer the following questions: ") <-- old way
print(f"Hi {name}. Please answer the following questions: ")
num_1 = int(input("What is your favourite number? "))
num_2 = int(input("What is your second favourite number? "))

# Add the stored numbers together
sum_of = num_1 + num_2

# Multiply the two numbers together
multiply = num_1 * num_2

# Display the results to the user
print(f"Your numbers added together are {sum_of}")
print(f"Your numbers multiplied together are {multiply}")


