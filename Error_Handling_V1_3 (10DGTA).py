# Program: Checking for a valid number
# Author: Juergen Lier
# Date: 27 June 2024
# Version 1.3

# TODO: Create a function to call every time I ask a user for a number
    # Create a for loop to ask for three numbers and add them together

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
'''
# Create a function to call every time I ask a user for a number. Recycling code
# It tries for a correct number until a valid one gets entered.
def test_float_num (question): # The parameter 'question' is a placeholder where my questions will insert when I call the function.
    error = "That is not a valid number."
    while True:
        print(question)
        try:
            num = float(input())
            if num > 0:
                break  
            else:
                print("Your number needs to be more than 0.")
        except ValueError: # If an incorrect value is entered, the program doesn't crash, but tries again.
            print(error)

    return(num) # When while loop stops, the value of num becomes available to the rest of the program.

#----------main program----------
print("Welcome, you will be asked to enter 3 numbers. The program will then add them together.")
total = 0 # This variable will get the numbers added to it as the user enters them.
for i in range(3): # i is the name of the loop.  3 is the nr of times I want to repeat this code.
    num = test_float_num("Please enter your value: ")
    print("The number ", i+1, "you entered is ", num)
    total += num # Adds the number that the user entered to the total.
print(f"The total of the numbers added is {total}")
print("The total of the nrs you entered is {}".format(total))