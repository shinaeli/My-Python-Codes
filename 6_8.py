pet_1 = {
    'animal_type': 'dog',
    'owner': 'james'
}
pet_2 = {
    'animal_type': 'cat',
    'owner': 'temi'
}
pet_3 = {
    'animal_type': 'monitor lizard',
    'owner': 'laolu'
}
pet_4 = {
    'animal_type': 'parrot',
    'owner': 'jolade'
}
pet_5 = {
    'animal_type': 'goat',
    'owner': 'wale'
}

pets = [pet_1, pet_2, pet_3, pet_4, pet_5]

for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['animal_type']}.")



