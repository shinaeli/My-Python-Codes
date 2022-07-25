alien_color = ['green', 'yellow', 'red']

player_color_choice = input('Enter a color: ').lower()

if player_color_choice == alien_color[0]:
    print("You've just earned 5 points.")
elif player_color_choice == alien_color[1]:
    print("You've just earned 10 points.")
elif player_color_choice == alien_color[2]:
    print("You've just earned 15 points.")
else:
    print('Invalid input!')