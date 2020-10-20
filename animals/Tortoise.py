from datetime import date
from animals import Animal
from movements import Walking

class Tortoise(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.date_added = date.today()
        self.shift = shift
        
    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def feed(self):
      return print(f'on {date.today()}, {self.name} was clapped for so it would eat its {self.food}')  
