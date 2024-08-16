class Vehicles():
   def __init__(self, make, model, year, price):
      self.make = make
      self.model = model
      self.year = year
      self.price = price
      
   def vehicle_make(self):
      if self.make == 'ford' or self.make == 'chevy' or self.make == 'tesla':
         return 'American Made'
      else:
         return 'Imported'
         
   def vehicle_model(self):
      return self.model
   
   def vehicle_year(self):
      if self.year >= 2000:
         return '21st century car!'
      else:
         return 'This car is old...'
      
   def vehicle_price(self, max_price):
      if self.price <= max_price:
         return 'it is within your budget price'
      else:
         return 'it is too expensive'
      
      
class Style(Vehicles):
   def __init__(self, make, model, year, price, num_doors):
      super().__init__(make, model, year, price)
      self.num_doors = num_doors
      
   def vehicle_doors(self):
      if self.num_doors == 4:
         return 'Family car'
      else:
         return 'Sport\'s car'
      
      
truck = Vehicles('ford', 'f-150', 2000, 100000)
print(f'The {truck.vehicle_make()}, {truck.vehicle_model()} is a {truck.vehicle_year()} and  {truck.vehicle_price(100000)}')

car = Style('toyota', 'camry', 2015, 20000, 4)
print(f'The {car.vehicle_make()}, {car.vehicle_model()} is a {car.vehicle_year()} and  {car.vehicle_price(20000)}. The {car.vehicle_model()} is consider to be a {car.vehicle_doors()}')

sports_car = Style('tesla', 'model s', 2020, 50000, 2)
print(f'The {sports_car.vehicle_make()}, {sports_car.vehicle_model()} is a {sports_car.vehicle_year()} and  {sports_car.vehicle_price(20000)}. The {sports_car.vehicle_model()} is consider to be a {sports_car.vehicle_doors()}')