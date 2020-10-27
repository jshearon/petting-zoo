class Wetlands:
  def __init__(self, name):
    self.name = name
    self.description = "Just keep swimming, just keep swimming"
    self.animals = list()
  
  def add_animal(self, animal):
    self.animals.append(animal)
