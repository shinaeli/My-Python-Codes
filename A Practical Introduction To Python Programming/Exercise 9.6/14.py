# Write a program to play the following simple game. The player starts with $100. On each
# turn a coin is flipped and the player has to guess heads or tails. The player wins $9 for each
# correct guess and loses $10 for each incorrect guess. The game ends either when the player
# runs out of money or gets to $200.

from random import choice

player_fund = 100
coin = ['Head', 'Tail']
while (player_fund != 0) or (player_fund == 200):
    toss_a_coin = input('toss a coin(enter "head" or "tail"): ').title()
    tossed_coin = choice(coin)
    if tossed_coin == toss_a_coin:
        player_fund += 9
        print(f'You just earned $9.')
        print(f'You now have ${player_fund}.')
    elif toss_a_coin == 'Q':
        print('Game ended!')
        break
    else:
        player_fund -= 10
        print(f'You just lost $10.')
        print(f'You now have ${player_fund}.')


