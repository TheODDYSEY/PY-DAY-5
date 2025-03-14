class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def display_info(self):
        return f"Smartphone Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB"