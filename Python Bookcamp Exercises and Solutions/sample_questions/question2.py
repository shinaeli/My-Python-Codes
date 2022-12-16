def question_2():
    print(f"Q2. What is the value of the expression: 1+(2*3)/4?")
    print('\n(a) 1.5\n(b) 3\n(c) 3.5\n(d) None')
    user_input = input('Type your answer(a/b/c/d): ')
    options = {
        'a': 1.5,
        'b': 3,
        'c': 3.5,
        'd': 'None'
    }
    if options[user_input] == 'None':
        return 'You are correct.'
    else:
        return 'You are wrong.'