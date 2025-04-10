class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Faris", 22)
print(person.age)
print(person.name)
print(type(person).__name__)