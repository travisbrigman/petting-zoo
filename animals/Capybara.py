from datetime import date
from animals import Animal

class Capybara(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.date_added = date.today()
        self.shift = shift
        self.walking = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      return print(f'on {date.today()}, {self.name} was gently snuggled so it would eat its {self.food}')  
