from datetime import date
from models.animal import Animal
  
class Crocodile(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food)
    self.slithering = True
    self.__chip_num = chip_num

  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  
  def __str__(self):
    return f"{self.name} is a {self.species}"
  
  @property
  def chip_num(self):
    try:
      return self.__chip_num
    except AttributeError:
      return 0
    
  @chip_num.setter
  def chip_num(self, num):
      if type(num) is int:
        self.__chip_num = num
      else:
        raise TypeError('Requires an integer')
