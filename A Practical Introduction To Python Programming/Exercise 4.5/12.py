# A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly
# how much candy is in the bowl, then you win all the candy. You ask the person in charge the
# following: If the candy is divided evenly among 5 people, how many pieces would be left
# over? The answer is 2 pieces. You then ask about dividing the candy evenly among 6 people,
# and the amount left over is 3 pieces. Finally, you ask about dividing the candy evenly among
# 7 people, and the amount left over is 2 pieces. By looking at the bowl, you can tell that there
# are less than 200 pieces. Write a program to determine how many pieces are in the bowl.

for count in range(5):
    user_input = float(input('Guess the total number of candy in the basket: '))
    if user_input % 5 == 2 and user_input % 6 == 3 and user_input % 7 == 2:
        print(f'You are right. There are {int(user_input)} candies in the bowl.')
    else:
        print('You are wrong.')