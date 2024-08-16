cities = list()
city = input('Enter a city: ').title()

while city != '0':
   if city in cities:
      print(f'{city} is already in the list')
   else:
      cities.append(city)
   city = input('Enter a city: ').lower()
cities.sort()

print(f'Here are the cities in alphabetical order: {cities}')