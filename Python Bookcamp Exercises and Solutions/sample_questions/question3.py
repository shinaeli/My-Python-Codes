def question_3():
    print(f"Q3. The set data type can hold duplicate values. The statement is: ")
    print('\n(a) False\n(b) True\n(c) Partially correct\n(d) None')
    user_input = input('Type your answer(a/b/c/d): ')
    options = {
        'a': 'False',
        'b': 'True',
        'c': 'Partially correct',
        'd': 'None'
    }
    if options[user_input] == 'True':
        return 'You are correct.'
    else:
        return 'You are wrong.'