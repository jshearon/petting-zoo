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


Bilbo = Whale("Bilbo", "Beluga Whale", "Whale Food")
Jaws = Shark("Jaws", "Great White Shark", "Shark Food")
Fabien = Goldfish("Fabien", "Goldfish", "Fish Food")
Saba = Eel("Saba", "Electric Eel", "Eel Food")
Alvin = Dolphin("Alvin", "Dolphin", "Dolphin Food")

Zeynep = Donkey("Zeynep", "Donkey", "midday", "Donkey Food")
Zaine = Monkey("Zaine", "Capuchin Monkey", "morning", "Monkey Food")
Anna = Ostrich("Anna", "Ostrich", "afternoon", "Ostrich Food")
Leonard = Llama("Leonard", "Llama", "morning", "Llama Food")
Bertie = Tiger("Bertie", "Bengal Tiger", "midday", "Tiger Food")

Sherlock = Snake("Sherlock", "Python", "Snake Food")
Wilbur = Lizard("Wilbur", "Lizard", "Lizard Food")
Madeline = Crocodile("Madeline", "Crocodile", "Croc Food")
Wilson = Turtle("Wilson", "Sea Turtle", "Turtle Food")
Woody = Gecko ("Woody", "Gecko", "Gecko Food")

roberto = Donkey("Roberto", "alpaca", "midday", "Donkey Food")
print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')

print(Wilson.feed())
print(Madeline)

print(Bertie)
