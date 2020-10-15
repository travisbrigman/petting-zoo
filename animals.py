from datetime import date

from walking import Llama, Capybara, Tortoise, Pig, Ermine
from slithering import Garden_Snake, Earthworm, Salamander, Python_Snake, Boa_Snake
from swimming import Fish, Alligator, Seahorse, Frog, Platypus
from attractions import PettingZoo, SnakePit, Wetlands

#walking🦙
june = Llama("June","Llama", "morning","Macaroons")
johnny = Capybara("Johnny","Capybara", "midday", "pumpkins")
raphael = Tortoise("Raphael","Tortoise", "afternoon", "pizza")
wilbur = Pig("Wilbur","Pig", "morning", "slop")
ernesto = Ermine("Ernesto","Ermine", "afternoon","popsicles")

#slithering🐍
sam = Garden_Snake("Sam", "Garden Snake", "tomatoes")  
errol = Earthworm("Errol", "Earthworm", "fertilizer")  
sal = Salamander("Sal", "Salamander", "flies")  
pippin = Python_Snake("Pippin", "Python Snake", "mouse")  
bruce = Boa_Snake("Bruce", "Boa Snake", "mouse")   

#swimming🐠
nemo = Fish("Nemo", "Fish", "plankton")
alan = Alligator("Alan", "Alligator", "steak")
cedric = Seahorse("Cedric", "Seahorse", "plankton")
fred = Frog("Fred", "Frog", "flies")
pedro = Platypus("Pedro", "Platypus", "gummie bears")

varmint_village = PettingZoo("Varmint Village")
slither_inn = SnakePit("Slither Inn")
critter_cove = Wetlands("Critter Cove")

varmint_village.add(june)

'''
for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')
'''

varmint_village.report
