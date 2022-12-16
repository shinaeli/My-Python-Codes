# A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
# items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
# program that asks the user how many items they are buying and prints the total cost.

no_of_items_bought = int(input('Provide the number of items bought: '))
if no_of_items_bought <= 0:
    print('Leave the store ASAP.')
elif 1 <= no_of_items_bought < 10:
    print(no_of_items_bought * 12)
elif 10 <= no_of_items_bought <= 99:
    print(no_of_items_bought * 10)
else:
    print(no_of_items_bought * 7)