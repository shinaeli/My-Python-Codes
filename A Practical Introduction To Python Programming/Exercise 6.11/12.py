# Write a program that asks the user to enter a word and then capitalizes every other letter of
# that word. So if the user enters rhinoceros, the program should print rHiNoCeRoS.

user_input = input('Provide a word: ')

output = ''
for count in range(0, len(user_input)):
    if count % 2 == 0:
        output += user_input[count]
    else:
        output += user_input[count].upper()

print(output)


# Provide a word: condoms
# cOnDoMs
# Provide a word: rhinoceros
# rHiNoCeRoS