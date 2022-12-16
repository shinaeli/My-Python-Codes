# Write a program that lets the user play Rock-Paper-Scissors against the computer. There
# should be five rounds, and after those five rounds, your program should print out who won
# and lost or that there is a tie.

from random import choice
items = ['Rock', 'Paper', 'Scissors']
for count in range(5):
    guess = choice(items)
    user_guess = input('Choose either "Rock", "Paper", or "Scissors": ')
    if user_guess == guess:
        print('You won!')
    else:
        print('You lost!')



