def grade(score):
   print('Your score is: ')
   if score > 0 and score <= 50:
      print('Below passing, Improve your grade!')
   elif score > 50 and score <= 70:
      print('Barely passing the class!')
   elif score > 70 and score <= 90:
      print('You have a passing grade!')
   else:
      print('Your are one of the best in the class!')
      
score = int(input('Enter your score: '))
grade(score)