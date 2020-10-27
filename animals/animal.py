from datetime import date

class Animal:
  def __init__(self, name, species, food, chip_num):
    self.name = name
    self.species = species
    self.food = food
    self.date_added = date.today()
    self.__chip_num = chip_num

  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
  
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
