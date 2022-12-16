# Write a program that asks the user to enter a string s and then converts s to lowercase,
# removes all the periods and commas from s, and prints the resulting string.

s = input('Provide a string: ')
low_case = s.lower()
for letter in low_case:
    if (letter == ',') or (letter == '.'):
        result = low_case.replace(letter, '')
print(result)
