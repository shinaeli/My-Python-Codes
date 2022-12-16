# Write a program that gets a string from the user containing a potential telephone number.
# The program should print Valid if it decides the phone number is a real phone number, and
# Invalid otherwise. A phone number is considered valid as long as it is written in the form
# abc-def-hijk or 1-abc-def-hijk. The dashes must be included, the phone number should contain
# only numbers and dashes, and the number of digits in each group must be correct. Test your
# program with the output shown below.
# Enter a phone number: 1-301-447-5820
# Valid
# Enter a phone number: 301-447-5820
# Valid
# Enter a phone number: 301-4477-5820
# Invalid
# Enter a phone number: 3X1-447-5820
# Invalid
# Enter a phone number: 3014475820
# Invalid

user_input = input('Provide a phone number: ')
splitted_str, checker = [], []
if '-' in user_input and 2 <= user_input.count('-') <= 3:
    splitted_str = user_input.split('-')
    for pos in range(len(splitted_str)):
        if pos == 0:
            # 'isdigit()' method returns 'True' if all the characters in a string are digits
            if (len(splitted_str[pos]) == 1 or len(splitted_str[pos]) == 3) and (splitted_str[pos].isdigit()):
                checker.append('valid')
            else:
                checker.append('invalid')
        elif (pos > 0) and (pos < (len(splitted_str) - 1)):
            if (len(splitted_str[pos]) == 3) and (splitted_str[pos].isdigit()):
                checker.append('valid')
            else:
                checker.append('invalid')
        elif pos == (len(splitted_str) - 1):
            if (len(splitted_str[pos]) == 4) and (splitted_str[pos].isdigit()):
                checker.append('valid')
            else:
                checker.append('invalid')
    if 'invalid' in checker:
        print('Invalid')
    else:
        print('Valid')
else:
    print('Invalid')

# print(splitted_str)
# print(checker)

# print(23.isnumeric())