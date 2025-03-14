## PLP PYTHON DAY 4: Class Design and Polymorphism

## Overview
This project demonstrates class design in Python by implementing three different classes: `Smartphone`, `Book`, and `Superhero`. Additionally, it showcases polymorphism through the use of animal and vehicle classes, each with a `move()` method defined differently.

## Classes

### Smartphone
- **Attributes**: `brand`, `model`, `storage`
- **Methods**: 
  - `display_info()`: Displays the smartphone's details.

### Book
- **Attributes**: `title`, `author`, `pages`
- **Methods**: 
  - `read()`: Simulates reading the book.

### Superhero
- **Attributes**: `name`, `power`, `city`
- **Methods**: 
  - `save_the_day()`: Simulates the superhero's actions.

## Polymorphism

### Animal
- **Abstract Class**: `Animal`
- **Method**: `move()`
  - **Subclasses**:
    - `Dog`: Implements `move()` to print "Running".
    - `Cat`: Implements `move()` to print "Pouncing".

### Vehicle
- **Abstract Class**: `Vehicle`
- **Method**: `move()`
  - **Subclasses**:
    - `Car`: Implements `move()` to print "Driving".
    - `Plane`: Implements `move()` to print "Flying".

## Running the Project
 Run the main files using Python:
   - For the main project: `python main.py`
   - For the polymorphism challenge: `python polymorphism/main.py`

## Examples of Usage
- Create instances of `Smartphone`, `Book`, and `Superhero` and call their respective methods to see their functionality.
- Create instances of `Dog`, `Cat`, `Car`, and `Plane` to demonstrate polymorphism through the `move()` method.

## Requirements
- Python 3.x

This project serves as a practical example of object-oriented programming principles, including class design and polymorphism in Python.