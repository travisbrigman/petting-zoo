class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return self.animals[-1]


class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "sleek and slithering creatures all around you"
        self.animals = list()

class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "If it swims and can be caught, it's in here"
        self.animals = list()

