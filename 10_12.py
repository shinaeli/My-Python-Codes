import json

try:
    with open('new_user_favorite.json') as favorite_file:
        content = json.load(favorite_file)

except FileNotFoundError:
    user_input = input('Provide your favorite number: ')
    with open('new_user_favorite.json', 'w') as favorite_file:
        json.dump(user_input, favorite_file)

else:
    print(f"Oh! Yes! I remember that your favorite number is: {content}.")


