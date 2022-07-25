cities = {
    'new_york': {
        'country': 'united states of america',
        'population': 8804190,
        'fact': 'it is the most populous city in the united states.'
    },
    'lagos': {
        'country': 'nigeria',
        'population': 15320128,
        'fact': 'it is the second most populous city in west africa, largest city in nigeria.'
    },
    'london': {
        'country': 'united kingdom',
        'population': 9000000,
        'fact': 'it is the smallest city in england.'
    }
}

for city in cities.keys():
    print(f'Few details about {city.title()}: ')
    print(f"It is located in {cities[city]['country'].title()}.")
    print(f"It has a population of {cities[city]['population']} people.")
    print(f"{cities[city]['fact'].title()}")

print('\n')

print('check the other approach below: '.title())

print('\n')


for city in cities.keys():
    print(f'Few details about {city.title()}: ')
    for detail in cities[city].keys():
        if type(cities[city][detail]) != str:
            print(f'{detail.title()}: {cities[city][detail]}')
        else:
            print(f'{detail.title()}: {cities[city][detail].title()}')





