from .Attraction import Attraction


class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    @property
    def last_critter_added(self):
        return self.animals[-1]

    def add_animal(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal} doesn\'t like to be petted, so please do not put it in the {self.name} attraction.')