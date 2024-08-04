guests = int(input('How many guests do you want to invite? '))
for i in range(guests):
   name = input('Enter name: ')
   age = int(input('Enter age: '))
   if age >= 18:
      print(f'Congrats {name} you can come to the party')
   else:
      print(f'Sorry {name} you can\'t come to the party')