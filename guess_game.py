guess_number = 9
guess_counter = 1
while guess_counter < 4:
    guess = input('Guess: ')
    guess_counter += 1
    if int(guess) == guess_number:
        print('You win')
        break
# This 'else' statement below executes if the while completely executes successfully without an immediate break
# That is if the while loop condition turns out to be false
else:
    print('Sorry you failed')

