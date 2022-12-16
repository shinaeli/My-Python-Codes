import random

print('Make a guess between 1 and 15 both inclusive.')

count = 0

while count < 3:
    guess = random.randint(1, 15)
    user_input = input('Make a guess: ')
    if int(user_input) == guess:
        print('Great! You are correct.')
        break
    else:
        print('You are wrong. Try again.')
        print(f'The correct guess is {guess}.')
    count += 1


