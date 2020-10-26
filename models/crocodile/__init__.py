from datetime import date
from models.animal import Animal
  
class Crocodile(Animal):
  def __init__(self, name, species, food):
    super().__init__(name, species, food)
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.slithering = True
    self.food = food

  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  
  def __str__(self):
    return f"{self.name} is a {self.species}"
