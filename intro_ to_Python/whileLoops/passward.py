password = input('Enter your password: ')

while password != 'password123':
   print('Access denied, You have entered the wrong password')
   password = input('Try again: ')

print('Access granted, Welcome')