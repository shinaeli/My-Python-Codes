favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people_poll = ['greg', 'james', 'lola']

for name in favorite_languages.keys():
    people_poll.append(name)

people_poll.insert(4, 'molly')
people_poll.insert(7, 'samuel')

print(people_poll)

people_to_take_poll = []

for people in people_poll:
    if people in favorite_languages.keys():
        print(f'Thank you for responding to our poll invitation. {people.title()}.')
    else:
        print(f"Dear {people.title()}, you're invited to take a poll at LCP head-quarters.")

