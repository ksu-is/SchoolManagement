import string
import random

# Define the set of allowed characters for the password
# This line was missing the variable name
CHARACTERS = string.ascii_letters + string.digits + '!@#$%~()*-+'

while True:
    try:
        # Added try-except to handle non-integer input for length
        length = int(input('Please enter your preferred password length : '))

        # Generate the password
        password = ''.join([random.choice(CHARACTERS) for i in range(length)])

        print('Your Password : {}'.format(password))

    except ValueError:
        print("Invalid input. Please enter a whole number for the length.")
        continue # Restart the loop for valid length input

    # Loop to ask the user if they want another password
    while True:
        answer = input('do you want another password (Y/n) : ').lower()

        if answer == 'n' or answer == 'y':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    # Exit the main loop if the answer is 'n'
    if answer == 'n':
        break

print("Thank you for using the password generator!")