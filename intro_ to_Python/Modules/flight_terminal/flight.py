from terminal import *

question = input('Would you like to check for your flight: ').lower()
while question != 'no':
   if question == 'yes':
      flight_check()
   else:
      print('You did not say yes')
   question = input('Would you like to check for your flight: ').lower()