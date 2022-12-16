# An anagram of a word is a word that is created by rearranging the letters of the original.
# For instance, two anagrams of idle are deli and lied. Finding anagrams that are real words is
# beyond our reach until Chapter 12. Instead, write a program that asks the user for a string
# and returns a random anagram of the string—in other words, a random rearrangement of the
# letters of that string

# import random
#
user_input = input('Provide a word: ').lower()
output = ''
#
# for count in range(0, len(user_input)):
#     guess_num = random.randint(0, len(user_input) - 1)
#     print(guess_num)
#     output += user_input[guess_num]
#
# print(output)

for count in range(len(user_input) - 1, -1, -1):
    first_letter = user_input[count]
    output += first_letter


