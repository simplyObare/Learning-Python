class Animal():
   def __init__(self, name, pet, sound):
      self.name = name
      self.pet = pet
      self.sound = sound
      
   def speak(self):
      if self.sound == None:
         print('Sound not known')
      else:
        print(self.sound)
      
   def pet_info(self):
      if self.sound == None:
         print(f'My pet {self.name} is a {self.pet}')
      else:
         print(f'My pet {self.name} is a {self.pet} and likes to {self.sound}')

      
class Fish(Animal):
   def swim(self):
      if self.sound == None:
         print('You are a fish')
      else:
         print('You are not a fish')
         
   def ocean(self):
      region = input('Enter ocean region: ')
      print(f'{self.name} is a {self.pet} who lives in the {region}')
      
fish = Fish('Nemo', 'Clown-fish', None)
fish.speak()
fish.pet_info()

fish.swim()
fish.ocean()