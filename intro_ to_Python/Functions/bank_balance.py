def bank_balance(balance):
   if balance >= 500:
      return True
   else:
      return False
   
bankers = int(input('Number of bank customers: '))
for i in range(bankers):
   first_name = input('Enter first name: ')
   balance = float(input('Enter balance: '))
   res = bank_balance(balance)
   
   print(f'Enough funds in {first_name}\'s account: {res}')
   if res == True:
      print('Don\'t worry you have enough funds')
   else:
      print('Your account is getting low, please deposit more funds into the account')