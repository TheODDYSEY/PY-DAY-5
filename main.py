# File: /python-project/python-project/src/main.py

from classes.smartphone import Smartphone
from classes.book import Book
from classes.superhero import Superhero

def main():
    # Create instances of Smartphone
    phone = Smartphone("Apple", "iPhone 14", "128GB")
    print(phone.display_info())

    # Create instances of Book
    book = Book("1984", "George Orwell", 328)
    book.read()

    # Create instances of Superhero
    hero = Superhero("Spider-Man", "Web-slinging", "New York")
    hero.save_the_day()

if __name__ == "__main__":
    main()