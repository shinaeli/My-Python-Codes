others_favorites = {
    'kemi': [12, 7, 42],
    'deoye': [18, 68, 13, 100],
    'adeola': [40, 24, 15],
    'jibola': [61, 73, 88, 1, 9],
    'samuel': [25, 44]
}

for name in others_favorites.keys():
    print(f"{name.title()}'s favorite numbers are: ")
    for num in others_favorites[name]:
        print(num)