# Write a program that takes a list of ten prices and ten products, applies an 11% discount to
# each of the prices displays the output like below, right-justified and nicely formatted.
# Apples $ 2.45
# Oranges $ 18.02
# ...
# Pears $120.03

user_prices = eval(input('provide ten prices: '))
user_products = eval(input('provide ten products: '))
for item in range(len(user_prices)):
    print(f'{user_products[item].title()}  ${round(user_prices[item] - (0.11 * user_prices[item]), 2)}')

# provide ten prices: [12, 90, 85, 17, 25, 40, 14.95, 22.8, 8.25, 110]
# provide ten products: ['apples', 'oranges', 'mangoes', 'bananas', 'pears', 'strawberries', 'pawpaws', 'coconuts', 'sugar canes', 'agbalumos']
# Apples  $10.68
# Oranges  $80.1
# Mangoes  $75.65
# Bananas  $15.13
# Pears  $22.25
# Strawberries  $35.6
# Pawpaws  $13.31
# Coconuts  $20.29
# Sugar Canes  $7.34
# Agbalumos  $97.9

