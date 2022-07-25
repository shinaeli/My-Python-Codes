from restaurant import Restaurant

restaurant1 = Restaurant('yetty MAma', 'wooden')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.number_served = 15
print(restaurant1.number_served)
restaurant1.set_number_served(20)
restaurant1.increment_number_served(10)
print(restaurant1.number_served)


# Yetty Mama
# wooden
# Yetty Mama Restaurant is open.
# 15
# 20
# 30
# 30

