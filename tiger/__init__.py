from datetime import date

class Tiger:
  def __init__(self, name, species, shift):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True
    self.shift = shift
