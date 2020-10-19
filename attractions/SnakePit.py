class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "sleek and slithering creatures all around you"
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)