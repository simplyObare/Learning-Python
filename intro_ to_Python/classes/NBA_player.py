class Player():
   def __init__(self, name, score):
      self.name = name
      self.score = score
      self.team = None
      
   def show_stats(self):
      print(f'{self.name} has an average of {self.score} points per game')
      print(f'He plays for the {self.team}')
      
   def select_team(self):
      team = input('Enter your team: ').title()
      self.team = team
      
player = Player('Lebron James', 30)
player.select_team()
player.show_stats()

player = Player('Magic Johnson', 25)
player.select_team()
player.show_stats()