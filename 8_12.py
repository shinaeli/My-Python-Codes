def order_sandwich(*orders):
    print(f"It's making {len(orders)} sandwich.")
    for order in orders:
        print(f'-{order.title()} Sandwich')
    # print(orders)


order_sandwich('egg-roll', 'fried cheese', 'pepperoni')
order_sandwich('macaroni', 'creamy tea', 'hamburger', 'pizza')
order_sandwich('coconut')
