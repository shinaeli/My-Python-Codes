sister = {
    'first_name': 'Oluwaseyi',
    'last_name': 'Omotosho',
    'age': 20,
    'city': 'Osogbo'
}

mother = {
    'first_name': 'Mary',
    'last_name': 'Omotoso',
    'age': 60,
    'city': 'Ado-Ekiti'
}

friend = {
    'first_name': 'Muyideen',
    'last_name': 'Moshood',
    'age': 27,
    'city': 'Aseese'
}

people = [sister, mother, friend]

for person in people:
    for detail, info in person.items():
        if type(info) != str:
            print(f'{detail.title()}: {info}')
        else:
            print(f'{detail.title()}: {info.title()}')


