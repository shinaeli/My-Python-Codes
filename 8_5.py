def describe_city(city, country='united states of america'):
    print(f'{city.title()} is located in {country.title()}.')


describe_city('los angeles')
describe_city('lagos', 'nigeria')
describe_city(city='cairo', country='egypt')

# Los Angeles is located in United States Of America.
# Lagos is located in Nigeria.
# Cairo is located in Egypt.