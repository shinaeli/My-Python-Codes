import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


for throw in range(3):
    throw_dice = Dice()
    print(throw_dice.roll())