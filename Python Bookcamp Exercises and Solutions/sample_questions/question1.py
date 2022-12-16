def question_1():
    print(f"Q1. What is the value of the expression: 2*3-4?")
    print('\n(a) 1\n(b) 2\n(c) 3\n(d) None')
    user_input = input('Type your answer(a/b/c/d): ')
    options = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 'None'
    }
    if options[user_input] == eval('2*3-4'):
        return 'You are correct.'
    else:
        return 'You are wrong.'