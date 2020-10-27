from animals import (
  Whale, 
  Shark, 
  Goldfish, 
  Eel, 
  Dolphin, 
  Donkey, 
  Monkey, 
  Llama, 
  Ostrich, 
  Tiger, 
  Snake, 
  Lizard, 
  Crocodile, 
  Turtle, 
  Gecko)
from attractions import PettingZoo, Wetlands, SnakePit

def create_zoo():
  def pettable_critters():
    list = []
    Zeynep = Donkey("Zeynep", "Donkey", "midday", "Donkey Food", 12345)
    Zaine = Monkey("Zaine", "Capuchin Monkey", "morning", "Monkey Food", 12345)
    Anna = Ostrich("Anna", "Ostrich", "afternoon", "Ostrich Food", 12345)
    Leonard = Llama("Leonard", "Llama", "morning", "Llama Food", 12345)
    Bertie = Tiger("Bertie", "Bengal Tiger", "midday", "Tiger Food", 12345) 
    list.extend([Zeynep, Zaine, Anna, Leonard, Bertie]) 
    return list

  petting_zoo = PettingZoo("Cuddle Town", "bla bla bla")
  petting_zoo.animals = pettable_critters()
  print(f"{petting_zoo.name}: {petting_zoo.description}")
  for animal in petting_zoo.animals:
    print(f"  *{animal.name} the {animal.species}")
  print(petting_zoo.last_critter_added)

  def water_critters():
    list = []
    Bilbo = Whale("Bilbo", "Beluga Whale", "Whale Food", 12345)
    Jaws = Shark("Jaws", "Great White Shark", "Shark Food", 12345)
    Fabien = Goldfish("Fabien", "Goldfish", "Fish Food", 12345)
    Saba = Eel("Saba", "Electric Eel", "Eel Food", 12345)
    Alvin = Dolphin("Alvin", "Dolphin", "Dolphin Food", 12345)
    list.extend([Bilbo, Jaws, Fabien, Saba, Alvin])
    return list
  
  wet_lands = Wetlands("Splash City",  "bla bla bla")
  wet_lands.animals = water_critters()
  print(f"{wet_lands.name}: {wet_lands.description}")
  for animal in wet_lands.animals:
    print(f"  *{animal.name} the {animal.species}")


  def slither_critters():
    list = []
    Sherlock = Snake("Sherlock", "Python", "Snake Food", 12345)
    Wilbur = Lizard("Wilbur", "Lizard", "Lizard Food", 12345)
    Madeline = Crocodile("Madeline", "Crocodile", "Croc Food", 12345)
    Wilson = Turtle("Wilson", "Sea Turtle", "Turtle Food", 12345)
    Woody = Gecko ("Woody", "Gecko", "Gecko Food", 12345)
    list.extend([Sherlock, Wilbur, Madeline, Wilson, Woody])
    Madeline.chip_num = 12
    print(Madeline.chip_num)
    Madeline.feed()
    Madeline.run()
    Madeline.swim()
    return list
  
  snake_pit = SnakePit("Fangs R Us",  "bla bla bla")
  snake_pit.animals = slither_critters()
  print(f"{snake_pit.name}: {snake_pit.description}")
  for animal in snake_pit.animals:
    print(f"  *{animal.name} the {animal.species}")

  pettable_critters()
  water_critters()
  slither_critters()  

  # Create a Goose
bob = Shark("Bob", "Land Shark", "watercress sandwiches", 12345)

# Create an attraction
varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal(bob)

for animal in varmint_village.animals:
    print(animal)
