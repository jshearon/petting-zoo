from datetime import date

class Eel:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.swimming = True
