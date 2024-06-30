# Program: Checking for a valid number
# Author: Juergen Lier
# Date: 27 June 2024
# Version 1.2

# TODO: Create a function to call every time I ask a user for a number

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
'''

# Create a function to call every time I ask a user for a number. Recycling code
# It tries for a correct number until a valid one gets entered.

def test_float_num (question): # The parameter 'question' is a placeholder where my questions will insert when I call the function.
    done = False
    error = "That is not a valid number."
    while not done:
        print(question)
        try:
            num = float(input())
            if num > 0:
                done = True  # Or use the word break
            else:
                print("Your number needs to be more than 0.")
        except ValueError: # If an incorrect value is entered, the program doesn't crash, but tries again.
            print(error)

    return(num) # When while loop stops, the value of num becomes available to the rest of the program.

#----------main program----------
# Call the function and use it in more than one question
num_1 = test_float_num("Please enter your 1st number:")
num_2 = test_float_num("Please enter your 2nd number:")

print(f"The 1st number you entered is {num_1} and the 2nd number you entered is {num_2}.")