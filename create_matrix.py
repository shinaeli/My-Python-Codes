for row in range(3):
    collector = []
    for column in range(3):
        collector.append(1)
    print(collector)

# Creating a matrix by using the user inputs
print('Please, provide only whole numbers')
# Request for the number of rows
give_rows = input('Enter a row: ')
# Request for the number of columns
give_columns = input('Enter a column: ')
# Convert the rows provided by the user into an integer
rows = int(give_rows)
# Convert the columns provided by the user into an integer
columns = int(give_columns)
# Check if the user provided the right type of data for either rows or columns
if type(rows) != int or type(columns) != int:
    # If the provided data-type is wrong
    print('Error! Invalid Input!')
else:
    # Create an empty list called 'matrix'
    matrix = []
    # Iterate through the number of rows provided by the user
    for row in range(rows):
        # For each iteration, create an empty list called 'rowList'
        rowList = []
        # Iterate through the number of columns provided by the user
        for column in range(columns):
            # For each iteration, ask the user to provide an input of his or her choice
            user_input = input('Provide an input: ')
            # Assign the provided 'user_input' to the 'rowList' list as an item
            rowList.append(user_input)
        # print(rowList)
        # Assign the fully-filled 'rowList' to the 'matrix' list as an item at the end
        # of each iteration of the outer loop 'row'
        matrix.append(rowList)
    # Print the fully-filled 'matrix' list to the console
    print(matrix)
    # Iterate the fully-filled 'matrix' list
    for colrow in matrix:
        # Print each item of the fully-filled 'matrix' list to the console
        print(colrow)
