class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "If it swims and can be caught, it's in here"
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)