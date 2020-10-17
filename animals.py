from datetime import date

from whale import Whale
from shark import Shark
from goldfish import Goldfish
from eel import Eel
from dolphin import Dolphin
from donkey import Donkey
from monkey import Monkey
from llama import Llama
from ostrich import Ostrich
from tiger import Tiger
from snake import Snake
from lizard import Lizard
from crocodile import Crocodile
from turtle import Turtle
from gecko import Gecko


Bilbo = Whale("Bilbo", "Beluga Whale")
Jaws = Shark("Jaws", "Great White Shark")
Fabien = Goldfish("Fabien", "Goldfish")
Saba = Eel("Saba", "Electric Eel")
Alvin = Dolphin("Alvin", "Dolphin")

Zeynep = Donkey("Zeynep", "Donkey", "midday")
Zaine = Monkey("Zaine", "Capuchin Monkey", "morning")
Anna = Ostrich("Anna", "Ostrich", "afternoon")
Leonard = Llama("Leonard", "Llama", "morning")
Bertie = Tiger("Bertie", "Bengal Tiger", "midday")

Sherlock = Snake("Sherlock", "Python")
Wilbur = Lizard("Wilbur", "Lizard")
Madeline = Crocodile("Madeline", "Crocodile")
Wilson = Turtle("Wilson", "Sea Turtle")
Woody = Gecko ("Woody", "Gecko")

roberto = Donkey("Roberto", "alpaca", "midday")
print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
