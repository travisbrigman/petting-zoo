from datetime import date

class Garden_Snake():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.walking = True   
    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Earthworm():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.walking = True   
    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Salamander():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.walking = True   
    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Python_Snake():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.walking = True   
    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"
        
class Boa_Snake():
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.walking = True 
    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"