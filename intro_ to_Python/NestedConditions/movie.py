movie_question = input('Do you want to watch a movie? ').lower()

if movie_question == 'yes':
   genre_question = input('What kind of movie do you want to watch? ').lower()
   
   if genre_question == 'comedy':
      print('I recommend you watch The Hangover')
   elif genre_question == 'horror':
      print('I recommend you watch The Conjuring')
   elif genre_question == 'action':
      print('I recommend you watch The Matrix')
   else:
      print('I don\'t have any recommendation for you')
else:
   print('Ok, then perhaps a TV show would be better')