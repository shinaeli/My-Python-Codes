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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate flavor', 'cupcake flavor', 'strawberry flavor']

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)


icecream1 = IceCreamStand('Tasty Creams', 'leather seat')
print(icecream1.restaurant_name)
print(icecream1.cuisine_type)
icecream1.display_flavors()
icecream1.open_restaurant()


# Tasty Creams
# leather seat
# chocolate flavor
# cupcake flavor
# strawberry flavor
# Tasty Creams Restaurant is open.

