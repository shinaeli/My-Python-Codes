class Person:
    def __init__(self, first_name, last_name, birth_year, sex, origin):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.sex = sex
        self.origin = origin

    def talk(self):
        return f'Hello! My name is {self.first_name} {self.last_name}. I am a {self.sex}. I came from {self.origin} and I am {2022 - self.birth_year}years old.'


person1 = Person('Richard', 'Williams', 1978, 'male', 'Chicago')
print(person1.talk())
person2 = Person('Whitney', 'Douglas', 1984, 'female', 'Tappahannock')
print(person2.talk())
print(person2.birth_year, person1.origin)