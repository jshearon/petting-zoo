from .attraction import Attraction
class PettingZoo(Attraction):
  def __init__(self, name, description):
        super().__init__(name, description)
  
  @property 
  def last_critter_added(self):
    return f"The laster critter added to {self.name}: {self.animals[-1]}"
