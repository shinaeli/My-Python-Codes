# Initialize a variable 'start' to be equal to true
start = True
# Initialize a 'while' loop
while start:
    # The program is aborted whenever a user enters the letter 'q'
    print('Enter "q" to quit')

    # Request for input from a user
    user_input = input('Provide a radius of your choice: ')

    if user_input == 'q':
        start = False
    else:
        # Otherwise execute the code inside the 'try' block
        try:
            area_of_circle = 3.142 * (float(user_input) ** 2)
        except ValueError:
            # Execute the code located in the 'except' block if the exception 'ValueError' is found
            print('You provided an invalid input. Try again.')
        # If there is no exception, print the code located in the 'else' block below
        else:
            print(area_of_circle)
