class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def move(self):
        print("Running")

class Cat(Animal):
    def move(self):
        print("Pouncing")