# A good program will make sure that the data its users enter is valid. Write a program that
# asks the user for a weight and converts it from kilograms to pounds. Whenever the user
# enters a weight below 0, the program should tell them that their entry is invalid and then ask
# them again to enter a weight. [Hint: Use a while loop, not an if statement].

start = True
while start:
    user_weight = float(input('Provide a weight in kilograms: '))
    if user_weight >= 0:
        print(f'The weight you provided is {user_weight * 2.20462}pounds.')
        start = False
    else:
        print('Your input is invalid. Please provide a valid input.')