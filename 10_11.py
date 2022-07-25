import json

user_input = input('Provide your favorite number: ')


with open('user_favorite.json', 'w') as favorite:
    json.dump(user_input, favorite)

with open('user_favorite.json') as favorite:
    # print(json.load(favorite))
    print(f"I know your favorite number. It's {json.load(favorite)}.")

