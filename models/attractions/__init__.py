class PettingZoo:
  def __init__(self, name):
    self.name = name
    self.description = "Your one stop shop for all things pettable"
    self.animals = list()
  
  def add_animal(self, animal):
    self.animals.append(animal)
  
  @property 
  def last_critter_added(self):
    return f"The laster critter added to {self.name}: {self.animals[-1]}"

class Wetlands:
  def __init__(self, name):
    self.name = name
    self.description = "Just keep swimming, just keep swimming"
    self.animals = list()
  
  def add_animal(self, animal):
    self.animals.append(animal)

class SnakePit:
  def __init__(self, name):
    self.name = name
    self.description = "Don't get too close folks, these critters have bite"
    self.animals = list()
  
  def add_animal(self, animal):
    self.animals.append(animal)
