from datetime import date

from models.whale import Whale
from models.shark import Shark
from models.goldfish import Goldfish
from models.eel import Eel
from models.dolphin import Dolphin
from models.donkey import Donkey
from models.monkey import Monkey
from models.llama import Llama
from models.ostrich import Ostrich
from models.tiger import Tiger
from models.snake import Snake
from models.lizard import Lizard
from .crocodile import Crocodile
from models.turtle import Turtle
from models.gecko import Gecko
from models.attractions import PettingZoo, Wetlands, SnakePit

class Animal:
  def __init__(self, name, species, food, chip_num):
    self.name = name
    self.species = species
    self.food = food
    self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self, num):
        pass


def create_zoo():
  def pettable_critters():
    list = []
    Zeynep = Donkey("Zeynep", "Donkey", "midday", "Donkey Food")
    Zaine = Monkey("Zaine", "Capuchin Monkey", "morning", "Monkey Food")
    Anna = Ostrich("Anna", "Ostrich", "afternoon", "Ostrich Food")
    Leonard = Llama("Leonard", "Llama", "morning", "Llama Food")
    Bertie = Tiger("Bertie", "Bengal Tiger", "midday", "Tiger Food") 
    list.extend([Zeynep, Zaine, Anna, Leonard, Bertie]) 
    return list

  petting_zoo = PettingZoo("Cuddle Town")
  petting_zoo.animals = pettable_critters()
  print(f"{petting_zoo.name}: {petting_zoo.description}")
  for animal in petting_zoo.animals:
    print(f"  *{animal.name} the {animal.species}")

  def water_critters():
    list = []
    Bilbo = Whale("Bilbo", "Beluga Whale", "Whale Food")
    Jaws = Shark("Jaws", "Great White Shark", "Shark Food")
    Fabien = Goldfish("Fabien", "Goldfish", "Fish Food")
    Saba = Eel("Saba", "Electric Eel", "Eel Food")
    Alvin = Dolphin("Alvin", "Dolphin", "Dolphin Food")
    list.extend([Bilbo, Jaws, Fabien, Saba, Alvin])
    return list
  
  wet_lands = Wetlands("Splash City")
  wet_lands.animals = water_critters()
  print(f"{wet_lands.name}: {wet_lands.description}")
  for animal in wet_lands.animals:
    print(f"  *{animal.name} the {animal.species}")


  def slither_critters():
    list = []
    Sherlock = Snake("Sherlock", "Python", "Snake Food")
    Wilbur = Lizard("Wilbur", "Lizard", "Lizard Food")
    Madeline = Crocodile("Madeline", "Crocodile", "Croc Food")
    Wilson = Turtle("Wilson", "Sea Turtle", "Turtle Food")
    Woody = Gecko ("Woody", "Gecko", "Gecko Food")
    list.extend([Sherlock, Wilbur, Madeline, Wilson, Woody])
    return list
  
  snake_pit = SnakePit("Fangs R Us")
  snake_pit.animals = slither_critters()
  print(f"{snake_pit.name}: {snake_pit.description}")
  for animal in snake_pit.animals:
    print(f"  *{animal.name} the {animal.species}")

  pettable_critters()
  water_critters()
  slither_critters()
