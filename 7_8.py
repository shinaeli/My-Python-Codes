sandwich_orders = ['french-fries sandwich',
                   'tuna sandwich',
                   'greeko sandwich',
                   'potato sandwich',
                   'hamburger sandwich']

finished_sandwiches = []

for order in sandwich_orders:
    print(f'I made your {order}.')
    finished_sandwiches.append(order)

for finished_sandwich in finished_sandwiches:
    print(f'{finished_sandwich.title()} was made.')



