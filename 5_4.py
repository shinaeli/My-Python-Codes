alien_color = ['green', 'yellow', 'red']

player_color_choice = input('Enter a color: ').lower()

if player_color_choice == alien_color[0]:
    print("You've just earned 5 points.")
else:
    print("You've just earned 10 points.")