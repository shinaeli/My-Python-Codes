class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f'{self.restaurant_name} Restaurant is open.')

    def set_number_served(self, number_newly_served):
        self.number_served = number_newly_served
        print(self.number_served)

    def increment_number_served(self, increased_served):
        self.number_served += increased_served
        print(self.number_served)


restaurant1 = Restaurant('yaKoYO', 'leather seats')
restaurant1.number_served = 20
print(restaurant1.number_served)
restaurant1.set_number_served(35)
restaurant1.increment_number_served(23)

# 20
# 35
# 58