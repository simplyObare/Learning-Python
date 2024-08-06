def good_deal(cost):
   if cost >= 50 and cost < 150:
      response = 'This is a good deal'
   elif cost >= 150:
      response = 'Overpriced'
   else:
      response = 'Cheap, buy now!'
   return response

store = input('Enter store name: ')
cost = float(input('Enter cost: '))
res = good_deal(cost)

print(f'{store} {res}')

if res == 'This is a good deal':
   print("Buy before it's too late!")