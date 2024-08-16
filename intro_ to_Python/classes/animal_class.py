class Animal():
   def __init__(self, name, pet, sound):
      self.name = name
      self.pet = pet
      self.sound = sound
      
   def speak(self):
      print(f'{self.name} {self.sound}\'s')
      
   def pet_info(self):
      print(f'My pet {self.name} is a {self.pet} and likes to {self.sound}')
      
Dog = Animal('Daisy', 'Dog', 'bark')
Cat = Animal('Coco', 'Cat', 'meow')

Dog.speak()
Dog.pet_info()
Cat.speak()
Cat.pet_info()