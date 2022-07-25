start = True

while start:
    print('Enter "q" or "Q" to quit.')
    # Request for user input ad assign it to 'user_fullname'
    user_fullname = input('Provide your first and last name: ')

    if user_fullname == 'q' or user_fullname == "Q":
        break
    else:
        # Capitalize the first letter of each word
        titled_fullname = user_fullname.title()

        # Create an empty string 'output'
        output = ''

        # Create a variable 'count' and set its value to be the index of the last character of 'titled_fullname' string
        count = len(titled_fullname) - 1

        # Initialize a 'while' loop that runs as long as count is greater than or equal to zero
        while count >= 0:
            # For each iteration, the character present at the current count index is added to 'output' string
            output += titled_fullname[count]
            # 'count' is reduced by 1 in each iteration
            count -= 1

        # The updated 'output' string is printed at the end of the 'while' loop
        print(output)


