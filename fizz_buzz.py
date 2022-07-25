def fizz_buzz():
    user_input = input('Provide a positive input: ')

    if (int(user_input) % 3 == 0) and (int(user_input) % 5 == 0):
        return 'FizzBuzz'
    elif int(user_input) % 5 == 0:
        return 'Buzz'
    elif int(user_input) % 3 == 0:
        return 'Fizz'


caller = fizz_buzz()
print(caller)