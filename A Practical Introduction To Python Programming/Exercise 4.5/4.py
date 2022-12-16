# Write a program that asks the user how many credits they have taken. If they have taken 23
# or less, print that the student is a freshman. If they have taken between 24 and 53, print that
# they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over

user_credit = float(input('Provide your number of credits taken: '))
if user_credit <= 23:
    print('You are a freshman.')
elif 24 <= user_credit <= 53:
    print('You are a sophomore.')
elif 54 <= user_credit <= 83:
    print('You are a junior.')
elif user_credit >= 84:
    print('You are a senior.')