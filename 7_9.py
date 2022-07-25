'pastrami'

sandwich_orders = ['french-fries sandwich',
                   'pastrami',
                   'tuna sandwich',
                   'greeko sandwich',
                   'pastrami',
                   'potato sandwich',
                   'pastrami',
                   'hamburger sandwich']

finished_sandwiches = []

print('Deli has run out of pastrami.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for order in sandwich_orders:
    finished_sandwiches.append(order)

print(finished_sandwiches)



