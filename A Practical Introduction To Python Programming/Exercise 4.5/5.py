# Generate a random number between 1 and 10. Ask the user to guess the number and print a
# message based on whether they get it right or not.

from random import randint
guess = randint(1, 10)
user_input = int(input('Make a guess between 1 and 10: '))
if user_input == guess:
    print('You guessed right.')
else:
    print('You are wrong.')
