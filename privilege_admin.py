from new_user import User


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can ban user', 'can delete post']

    def show_privileges(self):
            for privilege in self.privileges:
                print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.check_privileges = Privileges()


admin1 = Admin('geOrgE', 'miLLEr', 20, 'georgemillz@gmail.com')
admin1.describe_user()
admin1.check_privileges.show_privileges()