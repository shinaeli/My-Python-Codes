class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can ban user', 'can delete post']

    def show_privileges(self):
            for privilege in self.privileges:
                print(privilege)

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


class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.check_privileges = Privileges()


admin1 = Admin('daVId', 'JamES', 25, 'davidojay@gmail.com')
admin1.check_privileges.show_privileges()


# can add post
# can ban user
# can delete post




