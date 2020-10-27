from datetime import date
from .animal import Animal

class Shark(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.swimming = True

  def __str__(self):
    return f"{self.name} is a {self.species}"
