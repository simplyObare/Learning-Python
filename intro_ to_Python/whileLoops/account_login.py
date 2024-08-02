passcode = input('Enter your passcode: ')
while passcode != '1234' and passcode != '4321':
   print('Wrong passcode, try again')
   passcode = input('Enter your passcode: ')
print('Access granted')