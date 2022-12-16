def order_sandwich(*orders):
    print(f"It's making {len(orders)} sandwich.")
    for order in orders:
        print(f'-{order.title()} Sandwich')
    # print(orders)


order_sandwich('egg-roll', 'fried cheese', 'pepperoni')
order_sandwich('macaroni', 'creamy tea', 'hamburger', 'pizza')
order_sandwich('coconut')

# It's making 3 sandwich.
# -Egg-Roll Sandwich
# -Fried Cheese Sandwich
# -Pepperoni Sandwich
# It's making 4 sandwich.
# -Macaroni Sandwich
# -Creamy Tea Sandwich
# -Hamburger Sandwich
# -Pizza Sandwich
# It's making 1 sandwich.
# -Coconut Sandwich
