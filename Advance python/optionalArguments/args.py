# usage of *args - pass unspecified number of arguments

def my_function(*args):
   print(args)
   
my_function(10, 20, 30, 40, 50,'a','b','c')