expected_trip_cost = int(input('Enter your expected trip cost: '))

if expected_trip_cost < 350:
   print('Go on a stay-cation')
elif expected_trip_cost >= 350 and expected_trip_cost < 1000:
   print('Go on a road trip')
else:
   print('Catch a flight to Paris, France and visit some of the top-rated hotels in your city')
   
print('Have a nice trip!')   