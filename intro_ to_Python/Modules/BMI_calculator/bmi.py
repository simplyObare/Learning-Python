from past_function import show_results

people = int(input('Number of people: '))
for i in range(people):
   weight = float(input('Enter weight: '))
   height = float(input('Enter height: '))
   show_results(weight, height)