user_name = input('Enter your name: ')
invalid = '!@#$%^&*()_+'

for letter in user_name:
   if letter in invalid:
      print(f"""Invalid name, this character {letter} is not allowed""")
      break
else:
   print('Valid name')