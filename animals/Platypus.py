from datetime import date
from animals import Animal
from movements import Walking
from movements import Swimming

class Platypus(Animal, Walking, Swimming):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        Swimming.__init__(self)
        self.date_added = date.today()
        self.shift = shift
        

    def __str__(self):
        return f"{self.name} is a {self.species}"