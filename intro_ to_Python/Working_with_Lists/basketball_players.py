from random import *

players = input('Enter each player\'s name: ').split(' ')
player_amount = len(players)
teams = list()

for player in players:
   random_team = randint(1, 3)
   teams.append(random_team)
   
for i in range(player_amount):
   print(f'{players[i]} is on team {teams[i]}')