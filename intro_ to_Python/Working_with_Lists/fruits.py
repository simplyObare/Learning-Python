answers = list()
fruit = input('Enter the name of a fruit: ')

while fruit != 'quit':
   answers.append(fruit)
   
guess = input('Guess a fruit: ').lower()
for answer in answers:
   if guess == answer:
      print('Correct')
      break
   else:
      print('Wrong')
      break
      
   guess = input('Guess a fruit: ').lower()