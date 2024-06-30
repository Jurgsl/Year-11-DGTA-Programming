# Program: Checking for a valid number
# Author: Juergen Lier
# Date: 25 June 2024
# Version 1

# TODO: Test that a valid number is being entered.

'''
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
'''

# Checking for a valid number. If it is not a valid number, then try again.
done = False
while not done:
    print("Please enter your value as an integer: ")
    try:
        num = int(input())
        done = True
    except ValueError:
        print("That is not an integer.")
        continue

print(f"The integer you entered is {num}")