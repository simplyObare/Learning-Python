from time import *

stopwatch = input('1 - start, 0 - stop: ')

while stopwatch != '0':
   if stopwatch == '1':
      start_timer = time()
   stopwatch = input('0 - stop: ')
end_timer = time()
total = round((end_timer - start_timer), 2)
print(f'Total time: {total} seconds')