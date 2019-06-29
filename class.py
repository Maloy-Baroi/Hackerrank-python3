
class Attibutes:
    def walk(self):
        print("Walks")


class Dog(Attibutes):
    def __init__(self):
        print("Dog", end=" ")

class Cat(Attibutes):
    def __init__(self):
        print("Cat", end=" ")

dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.walk()