weight = input('Provide your weight: ')
unit = input('(L)bs or (K)g: ')
weight_integer = int(weight)
if unit.lower() == 'l' or unit.upper() == 'L':
    print(f'Your weight is {round(weight_integer * 0.454)}kilos.')
elif unit.lower() == 'k' or unit.upper() == 'K':
    print(f'Your weight is {round(weight_integer / 0.454)}lbs.')
else:
    print('Wrong Input')