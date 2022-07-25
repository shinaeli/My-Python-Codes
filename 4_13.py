offers = ('Eba', 'Rice', 'Pounded Yam', 'Bread and Beans', 'Amala')

for food in offers:
    print(food)

offers.append('Jollof Rice')
print(offers) #AttributeError: 'tuple' object has no attribute 'append'

offers = ('Eba', 'Fried Rice', 'Pounded Yam', 'Pizza', 'Amala')

for meal in offers:
    print(meal)