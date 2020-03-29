
from pprint import pprint

class Place:
  def __init__(self, description):
    self.description = description
    self.north = None
    self.south = None
    self.east = None
    self.west = None
  
  def setNorth(self, north):
    self.north = north
    return self

  def setSouth(self, south):
    self.south = south
    return self

  def setWest(self, west):
    self.west = west
    return self

  def setEast(self, east):
    self.east = east
    return self

  def goNorth(self):
    return self.north
   
  def goSouth(self):
    return self.south

  def goWest(self):
    return self.west
  
  def goEast(self):
    return self.east
    
  def look(self):
    print(self.description)
  

room1 = Place("You are in room1")
room2 = Place("You are in room2").setNorth(room1)
room1.setSouth(room2)


place = room1

statement = ""
while statement != "quit":
  place.look()
  #pprint(vars(place))
  
  statement = input("> ")
  

  if statement == "north" or statement == "n":
    place = place.goNorth()
  elif statement == "south" or statement == "s":
    place = place.goSouth()
  elif statement == "east" or statement == "e":
    place = place.goEast()
  elif statement == "west" or statement == "w":
    place = place.goWest()
  elif statement == "look" or statement == "l":
    place.look()

