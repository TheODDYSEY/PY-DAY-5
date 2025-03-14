# File: /python-project/python-project/src/polymorphism/main.py

from animal import Dog, Cat
from vehicle import Car, Plane

def main():
    # Create instances of animals
    dog = Dog()
    cat = Cat()

    # Demonstrate the move method for animals
    print("Animal Movements:")
    dog.move()
    cat.move()

    # Create instances of vehicles
    car = Car()
    plane = Plane()

    # Demonstrate the move method for vehicles
    print("\nVehicle Movements:")
    car.move()
    plane.move()

if __name__ == "__main__":
    main()