""" Домашнее задание №1 """

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f'{self.name} {self.age}'

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}")

    def is_adult(self):
        print(True if self.age >= 18 else False)


quasar1 = Person('Тима', 20, 'Bishkek')
quasar2 = Person('Умар', 16, 'Bishkek')
quasar3 = Person('Тилек', 22, 'Bishkek')

persons = [quasar1, quasar2, quasar3]

for person in persons:
    print(person)
    person.introduce()
    person.is_adult()