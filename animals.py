from datetime import date

from walking import Llama, Capybara, Tortoise, Pig, Ermine
from slithering import Garden_Snake, Earthworm, Salamander, Python_Snake, Boa_Snake
from swimming import Fish, Alligator, Seahorse, Frog, Platypus

#walking🦙
june = Llama("June","Llama", "morning")
johnny = Capybara("Johnny","Capybara", "midday")
raphael = Tortoise("Raphael","Tortoise", "afternoon")
wilbur = Pig("Wilbur","Pig", "morning")
ernesto = Ermine("Ernesto","Ermine", "afternoon")

#slithering🐍
sam = Garden_Snake("Sam", "Garden Snake")  
errol = Earthworm("Errol", "Earthworm")  
sal = Salamander("Sal", "Salamander")  
pippin = Python_Snake("Pippin", "Python Snake")  
bruce = Boa_Snake("Bruce", "Boa Snake")   

#swimming🐠
nemo = Fish("Nemo", "Fish")
alan = Alligator("Alan", "Alligator")
cedric = Seahorse("Cedric", "Seahorse")
fred = Frog("Fred", "Frog")
pedro = Platypus("Pedro", "Platypus")


print(f'{wilbur.name} the {wilbur.species} is available to pet during the {wilbur.shift} shift.')
