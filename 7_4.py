pizza_toppings = []

user_key = True

while user_key:
    user_topping = input('Please, provide a pizza topping of your choice: ').lower()
    if user_topping != 'quit':
        print(f'I will add {user_topping.title()} to your pizza.')
        pizza_toppings.append(user_topping)
        print(pizza_toppings)
    else:
        user_key = False


