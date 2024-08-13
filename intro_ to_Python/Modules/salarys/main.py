from functions import *

account = int(input('1 - run programme or 2 - quit programme: '))
while account != 2:
   employee = input('Name of employee: ')
   employee_type = input('Salary or Hourly: ').lower()
   
   if employee_type == 'hourly':
      time = int(input('Hours worked this month: '))
      pay = part_time(time)
   elif employee_type == 'salary':
      exp = int(input('Years on the job: '))
      pay = full_time(exp)
   else:
      print('Please visit HRM for any issues.')
      
   print(f'Employee Name: {employee} and Salary: {pay}')
   account = int(input('1 - run programme or 2 - quit programme'))