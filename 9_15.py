from random import choice, randint

items = [2, 15, 4, 8, 11, 3, 37, 27, 39, 10]

counter = 0
while True:
    spin = randint(1, 40)
    outcome = choice(items)
    counter += 1
    if spin == outcome:
        print(f'The winning ticket number is {outcome}.')
        print(f'The loop ran {counter} times to give you a winning ticket.')
        break
    else:
        continue
