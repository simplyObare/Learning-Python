class Rectangle():
   def __init__(self, length, width):
      self.length = length
      self.width = width
      
   def print_info(self):
      print(f'Length: {self.length}cm')
      print(f'Width: {self.width}cm')
      print(f'Perimeter: {2 * (self.length + self.width)}cm')
      print(f'Area: {self.length * self.width}cm^2')
      
   def update(self, length):
      self.update = (self.length - length) * self.width
      return self.update
   
a = int(input('Enter length: '))
b = int(input('Enter width: '))

rectangle = Rectangle(a, b)
rectangle.print_info()

c = int(input('Enter value to be subtracted from the previous length: '))
print(f'Update: {rectangle.update(c)}cm^2')