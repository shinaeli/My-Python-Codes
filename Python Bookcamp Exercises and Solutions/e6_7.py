detail = {
    'first name': 'Ayodeji',
    'last name': 'George',
    'phone': '08064592210',
    'age': 25,
    'email': 'djblack@gmail.com'
}

for items in detail.items():
    print(items)
# ('first name', 'Ayodeji')
# ('last name', 'George')
# ('phone', '08064592210')
# ('age', 25)
# ('email', 'djblack@gmail.com')
for item in detail.values():
    print(item)
# Ayodeji
# George
# 08064592210
# 25
# djblack@gmail.com
for item in detail.keys():
    print(item)
# first name
# last name
# phone
# age
# email