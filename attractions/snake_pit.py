class SnakePit:
  def __init__(self, name):
    self.name = name
    self.description = "Don't get too close folks, these critters have bite"
    self.animals = list()
  
  def add_animal(self, animal):
    self.animals.append(animal)
