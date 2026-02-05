class Car:
  def _init_(self, brand, model):
    self.brand = brand 
    self.model = model 

  def move(self):
    print("Drive!")

class Boat:
  def _init_(self, brand, model):
    self.brand = brand 
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def _init_(self, brand, model):
    self.brand = brand 
    self.model = model 

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")