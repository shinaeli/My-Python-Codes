# Creating a simple quiz

def quiz(expression):
    print(f'Predict the value of the expression: {expression}')
    user_input = input('Enter your answer: ')
    # 'eval' function solves an arithmetic expression that is wrapped as a string e.g. '10+(2**5)-7'
    if eval(user_input) == eval(expression):
        print('Correct answer.')
    else:
        print('Your answer is wrong.')
        print(f'The correct answer is {eval(expression)}.')


quiz('12*8%3')
quiz('12+(2*3)/4')



