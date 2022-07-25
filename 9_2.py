class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} Restaurant is open.')


restaurant1 = Restaurant('yaKoYO', 'leather seats')
restaurant2 = Restaurant('ojubOKUn', 'plastic chairs and tables')
restaurant3 = Restaurant('yeTTy mAmA', 'wooden chairs and tables')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Yakoyo
# leather seats
# Ojubokun
# plastic chairs and tables
# Yetty Mama
# wooden chairs and tables