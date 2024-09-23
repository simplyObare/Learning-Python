class Martian:

   def __init__(self, fn, ln):
      self.first_name = fn
      self.last_name = ln
      
   def __setattr__(self, name, value):
      print(f">>>>> Your set {name} = {value}")
      
m = Martian("Klaus", "Iserhon")