# A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
# the percent tip they want to leave. Then print both the tip amount and the total bill with the
# tip included.

meal_price = int(input('Provide the price of meal: '))
tip_percentage = int(input("Provide the tip's tip_percentage: "))

tip_amount = (tip_percentage / 100) * meal_price

print(f"The tip's amount is #{tip_amount} while the total price of the bill with the tip included is #{tip_amount + meal_price}.")

# Provide the price of meal: 2540
# Provide the tip's tip_percentage: 60
# The tip's amount is #1524.0 while the total price of the bill with the tip included is #4064.0.
# Provide the price of meal: 450
# Provide the tip's tip_percentage: 30
# The tip's amount is #135.0 while the total price of the bill with the tip included is #585.0.
