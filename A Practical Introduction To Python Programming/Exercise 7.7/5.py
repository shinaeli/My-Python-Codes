# Ask the user to enter a list of strings. Create a new list that consists of those strings with their
# first characters removed.

user_list = eval(input('Provide a list of words: '))

output_list = []

for word in user_list:
    new_word = word[1:]
    output_list.append(new_word)

print(output_list)

# Provide a list of words: ['fake', 'letter', 'seyi', 'roommate', 'JAMES']
# ['ake', 'etter', 'eyi', 'oommate', 'AMES']