with open('Sweeney Todd The Barber Of Fleet Street.txt') as sweeney_object_file:
    get_content = sweeney_object_file.read()
    print(get_content.count('the'))
    # 29139
    print(get_content.count('the '))
    # 19188
    print(get_content.lower().count('the'))
    # 31784