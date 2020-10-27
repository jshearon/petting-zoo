from datetime import date
from .animal import Animal
from movements import Walking, Swimming
  
class Crocodile(Animal, Walking, Swimming):
  def __init__(self, name, species, food, chip_num):
    Animal.__init__(self, name, species, food, chip_num)
    Swimming.__init__(self)
    Walking.__init__(self)

  def feed(self):
    print(f'{self.name} was fed super special {self.food} on {date.today().strftime("%m/%d/%Y")}')

  def run(self):
        print(f'{self} circumambulates')
  
  def __str__(self):
    return f"{self.name} is a {self.species}"
