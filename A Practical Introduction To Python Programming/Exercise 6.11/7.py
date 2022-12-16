# Write a program that asks the user to enter a word and determines whether the word is a
# palindrome or not. A palindrome is a word that reads the same backwards as forwards

user_input = input('Provide a word: ')

output = ''

for count in range(len(user_input) - 1, -1, -1):
    output += user_input[count]
    # print(count)

# print(output)
if output == user_input:
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")

# Provide a word: word
# 'word' is not a palindrome.
# Provide a word: deified
# 'deified' is a palindrome.
# Provide a word: racecar
# 'racecar' is a palindrome.
# Provide a word: kayak
# 'kayak' is a palindrome.
# Provide a word: madam
# 'madam' is a palindrome.



