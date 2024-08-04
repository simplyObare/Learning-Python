phone_num = input('Enter your phone number: ')
valid_digits = '0123456789+'

for digit in phone_num:
   if digit not in valid_digits:
      print('Invalid phone number')