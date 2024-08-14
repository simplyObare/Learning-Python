import random

winner = 36
current = random.randint(1, 50)
print(f'Winning number: {winner}')

if current == winner:
   print('you are the Winner')
else:
   print('Sorry you lost..., better luck next time')