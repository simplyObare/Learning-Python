accommodation_question = input('Would you like to stay in a hotel or in a resort? ').lower()

if accommodation_question == 'resort':
   max_price = int(input('How much do you want to spend? ').lower())
   
   if max_price >= 350:
      print('I recommend you check in at the six senses resort')
   else:
      print('I recommend you check in at the four seasons resort')
else:
   print('I recommend you check in at the Hilton Hotel')      