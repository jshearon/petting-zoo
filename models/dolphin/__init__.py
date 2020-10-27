from datetime import date
from models.animal import Animal

class Dolphin(Animal):
  def __init__(self, name, species, food):
    super().__init__(name, species, food)
    self.swimming = True

  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

  def __str__(self):
    return f"{self.name} is a {self.species}"
