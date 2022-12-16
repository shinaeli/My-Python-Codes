# Write a simple quote-of-the-day program. The program should contain a list of quotes, and
# when the user runs the program, a randomly selected quote should be printed.

from random import choice

quotes = ['I have always believed that each man makes his own happiness and is responsible for his own problems. '
          'It is a simple philosophy.',
          'Anger is the ultimate destroyer of your own peace of mind.',
          'Only one thing is guaranteed, that is that you will definitely not achieve the goal if you do not'
          ' take the shot',
          'Do not be afraid. Be focused. Be determined. Be hopeful. Be empowered.',
          'Children really brighten up a household. They never turn the lights off.',
          'Appreciate those early influences and what they have done for you']

print(choice(quotes))