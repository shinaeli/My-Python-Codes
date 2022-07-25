def build_profile(first_name, last_name, **profiles):
    profiles['first_name'] = first_name.title()
    profiles['last_name'] = last_name.title()
    return profiles


profile_1 = build_profile('oluwasina', 'omotosho', age=27, origin='osogbo'.title(), hometown='igbajo'.title(),
                          phone1='08141215891', phone2='09155214058')
print(profile_1)

# {'age': 27,
#  'origin': 'Osogbo',
#  'hometown': 'Igbajo',
#  'phone1': '08141215891',
#  'phone2': '09155214058',
#  'first_name': 'Oluwasina',
#  'last_name': 'Omotosho'}

