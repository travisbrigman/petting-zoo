from animals import Llama, Capybara, Tortoise, Pig, Ermine
from animals import Garden_Snake, Earthworm, Salamander, Python_Snake, Boa_Snake
from animals import Fish, Alligator, Seahorse, Frog, Platypus
from attractions import PettingZoo, SnakePit, Wetlands


#walking🦙
june = Llama("June","Llama", "morning","Macaroons",123456789)
johnny = Capybara("Johnny","Capybara", "midday", "pumpkins", 111111)
raphael = Tortoise("Raphael","Tortoise", "afternoon", "pizza", 222222)
wilbur = Pig("Wilbur","Pig", "morning", "slop", 333333)
ernesto = Ermine("Ernesto","Ermine", "afternoon","popsicles", 444444)

#slithering🐍
sam = Garden_Snake("Sam", "Garden Snake", "tomatoes", "bugs", 987)  
errol = Earthworm("Errol", "Earthworm", "fertilizer", "dirt", 654)  
sal = Salamander("Sal", "Salamander", "flies", "bugs", 321)  
pippin = Python_Snake("Pippin", "Python Snake", "mouse","mice", 000)  
bruce = Boa_Snake("Bruce", "Boa Snake", "mouse", "rats", 54654)   

#swimming🐠
nemo = Fish("Nemo", "Fish", "morning", "plankton", 101010)
alan = Alligator("Alan", "Alligator","afternoon", "steak", 788789)
cedric = Seahorse("Cedric", "Seahorse", "afternoon", "plankton", 555666)
fred = Frog("Fred", "Frog", "morning", "flies", 789321)
pedro = Platypus("Pedro", "Platypus", "morning", "gummie bears", 5556666555)

varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
slither_inn = SnakePit("Slither Inn", "sleek and slithering creatures all around you")
critter_cove = Wetlands("Critter Cove", "If it swims and can be caught, it's in here")

varmint_village.add_animal(june)
varmint_village.add_animal(johnny)
varmint_village.add_animal(alan)

slither_inn.add_animal(sam)
slither_inn.add_animal(errol)
slither_inn.add_animal(sal)
slither_inn.add_animal(pippin)
slither_inn.add_animal(bruce)

critter_cove.add_animal(nemo)
critter_cove.add_animal(alan)
critter_cove.add_animal(cedric)
critter_cove.add_animal(fred)
critter_cove.add_animal(pedro)



for animal in varmint_village.animals:
    print(animal)

for animal in slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')


alan.run()
alan.swim()