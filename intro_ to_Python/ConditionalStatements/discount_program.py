trip_type = input('Is your trip Business, Leisure or Personal? ').lower()
price =int(input('How much do you wish to spend on the trip? '))

if trip_type == 'business' and price >= 1200:
   print('You get a 15% discount')
else:
   print("You aren't qualified for a discount")