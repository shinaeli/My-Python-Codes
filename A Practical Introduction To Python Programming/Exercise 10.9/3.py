# Write a program that asks the user to enter a word. Rearrange all the letters of the word
# in alphabetical order and print out the resulting word. For example, abracadabra should
# become aaaaabbcdrr.

user_word = input('provide a word: ').lower()
# The 'list' function converts  the string into a list called 'splitted'
splitted = list(user_word)
print(splitted)
# 'splitted' is sorted in place
splitted.sort()
# the sorted 'splitted' list is joined to form a string
print(''.join(splitted))


# provide a word: abracadabra
# ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
# aaaaabbcdrr