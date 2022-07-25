list_of_pizzas = ['eforiro pizza', 'ponmo-kika pizza', 'bean pizza']

friend_pizzas = list_of_pizzas[:]

list_of_pizzas.append('chicken pizza')

friend_pizzas.append('vegetable pizza')

print(f'My favorite pizza are: {list_of_pizzas}')

for pizza in list_of_pizzas:
    print(pizza)

print(f'My favorite pizza are: {friend_pizzas}')

for pizza in friend_pizzas:
    print(pizza)