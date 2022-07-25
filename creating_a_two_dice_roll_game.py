import random
# Initialize a 'Dice' class
class Dice:
    # Create a method called 'roll'
    def roll(self):
        # Generate random numbers from 1 to 6 and wrap them in a tuple using a formatted string format
        return f'({random.randint(1, 6)}, {random.randint(1, 6)})'

# Assuming each player has a chance of rolling the two dice with only three trials
for trial in range(1, 4):
    # For each trial, create an instance called 'dice_throw'
    dice_throw = Dice()
    # On the instance created, call the 'roll' method
    print(dice_throw.roll())

