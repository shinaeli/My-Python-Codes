def city_country(city, country):
    return f'"{city.title()}, {country.title()}"'


call_1 = city_country('lagos', 'nigeria')
print(call_1)
call_2 = city_country('chicago', 'united states of america')
print(call_2)
call_3 = city_country('cairo', 'egypt')
print(call_3)

# "Lagos, Nigeria"
# "Chicago, United States Of America"
# "Cairo, Egypt"