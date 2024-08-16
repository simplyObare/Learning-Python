from time import sleep

class Agent():
   def __init__(self, name, health, car):
      self.name = name
      self.health = health
      self.car = car
      
   def agent_info(self):
      print(f'Welcome Agent: {self.name}')
      print(f'Your Health is: {self.health}')
      print(f'Your car choice is: {self.car}')
      
      
class Spy(Agent):
   def __init__(self, name, health, car, agency, location): 
       super().__init__(name, health, car)
       self.agency = agency
       self.location = location
       self.killed = False
       
   def assassinate(self, bad_guy):
      if bad_guy.health > 0:
         bad_guy.health -= 20
         print(f'{bad_guy.name} has lost 20 from his health')
         print(f'{bad_guy.name} has a health of {bad_guy.health}')
         
         if bad_guy.health <= 0:
            self.killed = True
            print(f'{bad_guy.name} has been killed')   
       
      
      
james_bond = Spy('James Bond', 100, 'Ferrari', 'MI-6', 'London')
ethan_hunt = Spy('Ethan Hunt', 40, 'Porsche', 'CIA', 'Spain')

james_bond.agent_info()
ethan_hunt.agent_info()
sleep(5)

while ethan_hunt.health > 0:
   james_bond.assassinate(ethan_hunt)
   ethan_hunt.assassinate(james_bond)
   sleep(2)