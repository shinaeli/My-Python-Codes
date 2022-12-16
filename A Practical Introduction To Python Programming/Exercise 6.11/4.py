# Write a program that asks the user to enter a word and prints out whether that word contains
# any vowels.

vowels = ['a', 'e', 'i', 'o', 'u']
user_input = input('Provide just a word: ')
for each in user_input:
    if each in vowels:
        print(f'{user_input} contains a vowel.')
        break
