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
