from random import randint

passenger = input('Enter passenger name (quit to quit): ')

while passenger != 'quit':
   flight_number = randint(1, 3)
   print(f'Flight {flight_number} for {passenger}')
   passenger = input('Enter passenger name (quit to quit): ')