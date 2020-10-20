from datetime import date
from movements import Swimming
from movements import Walking
from animals import Animal

class Capybara(Animal, Walking, Swimming):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        self.date_added = date.today()
        self.shift = shift
        

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
      return print(f'on {date.today()}, {self.name} was gently snuggled so it would eat its {self.food}')  
