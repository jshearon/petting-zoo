from datetime import date
from .animal import Animal

class Dolphin(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.swimming = True

  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

  def __str__(self):
    return f"{self.name} is a {self.species}"
