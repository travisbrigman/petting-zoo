from datetime import date
from animals import Animal

class Platypus(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.date_added = date.today()
        self.shift = shift
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"