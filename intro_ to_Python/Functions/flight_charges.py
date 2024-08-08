def flight_charges(price):
   upgrade = input('Would you like to upgrade: ')
   if upgrade == 'yes':
      price += 99
      
   baggage = input('Do you have any baggage: ')
   if baggage == 'yes':
      price += 35
   
   tax = (price * 0.08) + price
   return tax

price = int(input('Enter base fare: '))
grand_total = flight_charges(price)
print(f'Total fare: {grand_total}')