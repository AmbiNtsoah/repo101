class Person:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

    def introduce_self(self):
        print(f'Hello, I am {self.name}, I am {self.age} yo and I like {self.hobbies}')