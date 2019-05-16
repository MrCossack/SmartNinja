class Animal:
    count = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count.append(name)

    def get_number_animals(self):
        return len(self.count)

    def communicate(self):
        return "hello"

class Dog(Animal):
    def __init__(self, name, age, pow):
        super().__init__(name, age)
        self.pow = pow

    def communicate(self):
        return "Wuff"

class Fish(Animal):
    def __init__(self, name, age, fin):
        super().__init__(name, age)
        self.fin = fin

#animals = [Animal("bello", 23), Animal("Goldi", 4)]
a = Dog("bello", 23, 4)
b = Fish("Goldi", 4, 8)

print(a.get_number_animals())
print(b.name)
print(a.communicate())
print(b.communicate())