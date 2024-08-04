for i in range(3):
   username = input('Enter username: ')
   passcode = input('Enter passcode: ')
   if username == 'admin' and passcode == '1234':
      print('Access granted, Welcome admin')
      break

if username != 'admin' or passcode != '1234':
   print('Access denied, You are not the admin')