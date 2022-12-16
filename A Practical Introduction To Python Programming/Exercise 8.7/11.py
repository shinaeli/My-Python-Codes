# Section 8.3 described how to use the shuffle method to create a random anagram of a string.
# Use the choice method to create a random anagram of a string.

from random import choice

user_str = input('Provide a word: ')
splitted_str, chosen_list = [], []
for item in user_str:
    splitted_str.append(item)
# print(splitted_str)
for count in range(len(splitted_str)):
    chosen_str = choice(splitted_str)
    check_count = splitted_str.count(chosen_str)
    if chosen_list.count(chosen_str) < check_count:
        chosen_list.append(chosen_str)
    else:
        continue
print(chosen_list)
print(''.join(chosen_list))

Provide a word: peace
['p', 'a', 'c']
pac
['e', 'p', 'e']
epe
Provide a word: peace
['c', 'e', 'e']
cee
Provide a word: peace
['a', 'p', 'e']
ape
Provide a word: peace
['a', 'p', 'e', 'c']
apec
Provide a word: peace
['c', 'a', 'p']
cap


# print(['t', 'h', 'e', 'r', 'e'].count('e') > 2)




