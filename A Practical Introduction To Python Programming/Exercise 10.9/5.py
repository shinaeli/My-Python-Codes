# Use the following two lists and the format method to create a list of card names in the format
# card value of suit name (for example, 'Two of Clubs').
# suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# values = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
# 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

from random import choice

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

for item in values:
    print(f'{item} of {choice(suits)}')

# One of Clubs
# Two of Clubs
# Three of Diamonds
# Four of Diamonds
# Five of Clubs
# Six of Spades
# Seven of Clubs
# Eight of Hearts
# Nine of Clubs
# Ten of Clubs
# Jack of Spades
# Queen of Clubs
# King of Clubs
# Ace of Diamonds




