class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def describe_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()} is {self.age}years old. Mail: {self.email}.')

    def greet_user(self):
        print(f'Welcome! {self.first_name.title()} {self.last_name.title()}.')


user1 = User('freDrICK', 'FoLAwE', 24, 'folawe24@gmail.com')
user2 = User('MarY', 'WIlliaMs', 28, 'williemary@yahoo.com')
user3 = User('tomI', 'cOKer', 19, 'tomcoke@gmail.com')

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()

# Fredrick Folawe is 24years old. Mail: folawe24@gmail.com.
# Mary Williams is 28years old. Mail: williemary@yahoo.com.
# Tomi Coker is 19years old. Mail: tomcoke@gmail.com.
# Welcome! Fredrick Folawe.
# Welcome! Mary Williams.
# Welcome! Tomi Coker.