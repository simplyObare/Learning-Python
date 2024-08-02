item1 = int(input('Enter the price of item 1: '))
item2 = int(input('Enter the price of item 2: '))
item3 = int(input('Enter the price of item 3: '))

total = item1 + item2 + item3

if item1 < item2 and item2 < item3:
   total = total * 0.5
   print('You get 50% discount')
 
if item1 > item2 and item2 > item3:
   total = total * 0.33 
   
print('Your total cost is: ',total)