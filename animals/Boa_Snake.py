from datetime import date
from movements import Slithering
from animals import Animal

class Boa_Snake(Animal, Slithering):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        self.date_added = date.today()
        self.shift = shift

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"