from datetime import date
from animals import Animal

class Tortoise(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.date_added = date.today()
        self.shift = shift
        self.walking = True
    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def feed(self):
      return print(f'on {date.today()}, {self.name} was clapped for so it would eat its {self.food}')  
