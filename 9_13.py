from random import randint


class Die:
    def __init__(self, side=6):
        self.side = side

    def roll_die(self):
        print(randint(1, self.side))


die1 = Die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()

die2 = Die(10)
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()

die3 = Die(20)
die3.roll_die()
die3.roll_die()
die3.roll_die()
die3.roll_die()
die3.roll_die()
die3.roll_die()
die3.roll_die()
die3.roll_die()
die3.roll_die()
die3.roll_die()





