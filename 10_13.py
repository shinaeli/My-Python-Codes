import json


def get_stored_user():
    try:
        with open('usernames.json') as usernames_file:
            content = json.load(usernames_file)
    except FileNotFoundError:
        return None
    else:
        return content.title()


def get_new_username():
    user_name = input('Provide a username: ')
    with open('usernames.json', 'w') as usernames_file:
        json.dump(user_name, usernames_file)
    return  user_name


def greet_user():
    output = get_stored_user()
    if output:
        print(f"Welcome back. {output}!")
    else:
        new_user = get_new_username()
        print(f"We'll remember you when you come back, {new_user.title()}!")


greet_user()