# Write a program that has a list of ten words, some of which have repeated letters and some
# which don’t. Write a program that picks a random word from the list that does not have any
# repeated letters.

from random import choice
user_list = eval(input('Enter any random ten words: '))

start = True
while start:
    picked_word = choice(user_list)
    for letter in picked_word:
        if picked_word.count(letter) > 1:
            new_word = choice(user_list)
            picked_word = new_word
            break
    else:
        print(picked_word)
        start = False

# Enter any random ten words: ['patricia', 'gomez', 'farther', 'guns', 'roses', 'properly', 'heaven', 'death', 'Jesus', 'God']
# death
# Enter any random ten words: ['patricia', 'gomez', 'farther', 'guns', 'roses', 'properly', 'heaven', 'death', 'Jesus', 'God']
# God
# Enter any random ten words: ['patricia', 'gomez', 'farther', 'guns', 'roses', 'properly', 'heaven', 'death', 'Jesus', 'God']
# guns

