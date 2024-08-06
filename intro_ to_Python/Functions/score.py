def total_points(game_score):
   points = 0
   while game_score != 0:
      if game_score >= 5 and game_score <= 10:
         points += 2
      if game_score > 10 and game_score <= 20:
         points += 3
      game_score = int(print('Enter game score: '))
   return points

score = int(input('Enter score: '))
game_points = total_points(score)

print(f'Game points: {game_points}')