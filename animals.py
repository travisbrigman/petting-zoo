from datetime import date

from walking import Llama, Capybara, Tortoise, Pig, Ermine
from slithering import Garden_Snake, Earthworm, Salamander, Python_Snake, Boa_Snake
from swimming import Fish, Alligator, Seahorse, Frog, Platypus

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


print(f'{wilbur.name} the {wilbur.species} is available to pet during the {wilbur.shift} shift.')
print(f'{raphael.name} the {raphael.species} is available to pet during the {raphael.shift} shift.')



print(june.feed())
print(johnny.feed())
print(raphael.feed())
print(wilbur.feed())
print(ernesto.feed())

print(nemo.feed())
print(alan.feed())
print(cedric.feed())
print(fred.feed())
print(pedro.feed())

print(sam.feed())
print(errol.feed())
print(sal.feed())
print(pippin.feed())
print(bruce.feed())

print(sam)