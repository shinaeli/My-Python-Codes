# Create a dictionary called 'nums_store'
nums_store = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
              '9': 'nine', '0': 'zero', '+': 'plus'}
# Create a variable 'user_input' to request for user's phone number
user_input = input('Phone: ') #08141215891
# Create an empty string called 'output'
output = ''
# Iterate through the 'user_input' details provided by the user
for char in user_input:
    # For each iteration, get the value of current item in the 'nums_store' dictionary
    # and concatenate it with the 'output' variable
    output += nums_store[char]
    # Concatenate a space again to the updated 'output' variable
    output += ' '
# Print the updated 'output' variable to the console
print(f'{output}') #zero eight one four one two one five eight nine one