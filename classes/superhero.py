class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def save_the_day(self):
        return f"{self.name} uses {self.power} to save the day in {self.city}!"