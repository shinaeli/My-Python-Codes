def get_extension():
    user_input = input("Provide a filename with its extension: ")

    dot_index = user_input.find('.')

    print(user_input[dot_index + 1:])


get_extension()
