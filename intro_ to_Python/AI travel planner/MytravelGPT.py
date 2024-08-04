print('Welcome to Mytravel GPT, your personal travel assistant. How can I help you today?')
enter = int(input('Enter 1 to continue or 0 to exit: '))

while enter == 1:
   destination = input('Do you have a destination in mind?: ').lower()
   if destination == 'yes':
      print('Ok, let\'s get started')
      transport = input('What mode of transportation do you prefer(plane, car or train)?: ').lower()
      if transport == 'plane':
         class_type = input('Are you on first, business or economy class?: ').lower()
         luggage = input('Enter luggage weight in kg: ').lower()
         if luggage >= 21 and class_type == 'business' or class_type == 'first':
            print('Great, you can have more luggage in this class')
         elif luggage < 21 and class_type == 'business' or class_type == 'first':
            print('Ok, you can bring more if you want')
         else:
            print('Warning!, you may have to much luggage')
      elif transport == 'train':
         seat_class = input('business or economy?: ').lower()
         if seat_class == 'business':
            print('Great!, more comfort')
         elif seat_class == 'economy':
            print('You save more this way')
         else:
            print('We dont have that class')
      elif transport == 'car':
         print('Road trips are fun!')
         num_people = int(input('How many people are in your group?: '))
         if num_people <= 5:
            print('Great, you could rent a car')
         else:
            print('You may need to rent a van or a mini-bus')
      else:
         print('We dont have that transport option')
   else:
      print('Ok, I can help you choose a destination!')
      trip_type = input('Would you like a beach vacation, a city trip or an adventure (answer: beach, city or adventure)?: ').lower()
      if trip_type == 'beach':
         print('How about Hawaii?')
         beach_type = input('Do you prefer a popular or remote beach? (answer: popular or remote): ').lower()
         if beach_type == 'popular':
            print('Check out Waikiki Beach near Honolulu')
         elif beach_type == 'remote':
            print('Check out Kailua-Kona or Maui Beach near Honolulu')
         else:
            print('We dont have that beach option')
      elif trip_type == 'city':
         print('Head out to New York City')
         print('New York!, New York!').capitalize()
         activity = input('Would you like an indoor or outdoor activity (answer: indoor or outdoor)?: ').lower()
         if activity == 'indoor':
            print('Check out the Metropolitan Museum of Art')
         elif activity == 'outdoor':
            print('Check out the Central Park')
         else:
            print('We dont have that activity option')
      elif trip_type == 'adventure':
         print('Head out to Yosimite National Park, Arizona')
         outdoor_activity = input('''which of the following outdoor activities would you like to do? Hiking or Camping?: ''').lower()
         if outdoor_activity == 'hiking':
            print('Try hiking Half Dome')
         elif outdoor_activity == 'camping':
            print('Check out the many camping sites within the park')
         else:
            print('That activity is not offered')
      else:
         print('We dont have that trip type')
         
   print('Answer the question correctly to win a free trip')
   for i in range(1, 4):
      if input('What is the largest desert in the world? ').lower() == 'Antarctic':
         print('Correct,You win a trip to Paris, France!')
         
   enter = int(input('Enter 1 to continue or 0 to exit: '))
   
print('Enjoy your trip')
print('Thank you for using Mytravel GPT. Goodbye!')