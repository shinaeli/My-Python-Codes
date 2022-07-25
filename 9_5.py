class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()} is {self.age}years old. Mail: {self.email}.')

    def greet_user(self):
        print(f'Welcome! {self.first_name.title()} {self.last_name.title()}.')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)


user1 = User('freDrICK', 'FoLAwE', 24, 'folawe24@gmail.com')
user1.increment_login_attempts() #1
user1.increment_login_attempts() #2
user1.increment_login_attempts() #3
user1.increment_login_attempts() #4
user1.increment_login_attempts() #5
user1.increment_login_attempts() #6
print(user1.login_attempts) #6
user1.reset_login_attempts() #0