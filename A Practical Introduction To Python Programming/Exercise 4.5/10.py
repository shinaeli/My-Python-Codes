#  Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do. After each, the program should tell them
# whether they got it right or wrong and what the correct answer is.
# Question 1: 3 x 4 = 12
# Right!
# Question 2: 8 x 6 = 44
# Wrong. The answer is 48.
# ...
# ...
# Question 10: 7 x 7 = 49
# Right.

from random import randint
for item in range(1, 11):
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    question = num_1 * num_2
    answer = int(input(f'Question {item}: {num_1} x {num_2} = '))
    if answer == question:
        print('Right.')
    else:
        print(f'Wrong. The answer is {question}.')


# Question 1: 3 x 6 = 18
# Right.
# Question 2: 5 x 6 = 30
# Right.
# Question 3: 8 x 10 = 80
# Right.
# Question 4: 6 x 9 = 54
# Right.
# Question 5: 9 x 9 = 80
# Wrong. The answer is 81.
# Question 6: 1 x 7 = 7
# Right.
# Question 7: 9 x 8 = 72
# Right.
# Question 8: 7 x 6 = 42
# Right.
# Question 9: 8 x 4 = 32
# Right.
# Question 10: 5 x 3 = 15
# Right.
