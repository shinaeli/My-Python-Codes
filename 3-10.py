list_of_countries = ['South Africa', 'Nigeria', 'Egypt', 'Korea', 'Belgium']

print(len(list_of_countries)) #5

list_of_countries.append('Mali')
list_of_countries.append('Senegal')
print(list_of_countries) #['South Africa', 'Nigeria', 'Egypt', 'Korea', 'Belgium', 'Mali', 'Senegal']
print(len(list_of_countries)) #7

list_of_countries.insert(3, 'Ghana')
print(list_of_countries) #['South Africa', 'Nigeria', 'Egypt', 'Ghana', 'Korea', 'Belgium', 'Mali', 'Senegal']
print(len(list_of_countries)) #8

list_of_countries[2] = 'Israel'
print(list_of_countries) #['South Africa', 'Nigeria', 'Israel', 'Ghana', 'Korea', 'Belgium', 'Mali', 'Senegal']

removed_country = list_of_countries.pop()
print(list_of_countries)
print(removed_country) #Senegal
print(len(list_of_countries)) #7
removed_country2 = list_of_countries.pop(4)
print(removed_country2) #Korea
print(len(list_of_countries)) #6
print(list_of_countries) #['South Africa', 'Nigeria', 'Israel', 'Ghana', 'Belgium', 'Mali']
print(list_of_countries[2]) #Israel
print(list_of_countries[8]) #IndexError: list index out of range
