class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f'{self.restaurant_name} Restaurant is open.')


restaurant1 = Restaurant('yaKoYO', 'leather seats')

print(restaurant1.restaurant_name)

print(restaurant1.cuisine_type)

restaurant1.describe_restaurant()

restaurant1.open_restaurant()

# Yakoyo
# leather seats
# Yakoyo
# leather seats
# Yakoyo Restaurant is open.

