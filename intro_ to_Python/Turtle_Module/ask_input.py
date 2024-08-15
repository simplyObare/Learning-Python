from turtle import *

def square(t, size, color):
   for i in range(4):
      t.forward(size)
      t.color(color)
      t.left(90)
      
def triangle(t, size, color):
   for i in range(3):
      t.forward(size)
      t.color(color)
      t.left(120)
      
def rectangle(t, length, width, color):
   for i in range(4):
      if i % 2 == 0:
         t.forward(length)
         t.color(color)
         t.left(90)
      else:
         t.forward(width)
         t.color(color)
         t.left(90)
         
def circle(t, radius, color):
      t.circle(radius)
      t.color(color)
      t.left(1)
      
ask = input('Pick a shape you want to draw: ').lower()
t = Turtle()
while ask != 'quit':
   if ask == 'square':
      size = int(input('Enter the size: '))
      color = input('Enter the color: ')
      square(t, size, color)
      
   elif ask == 'triangle':
      size = int(input('Enter the size: '))
      color = input('Enter the color: ')
      triangle(t, size, color)
      
   elif ask == 'rectangle':
      length = int(input('Enter the length: '))
      width = int(input('Enter the width: '))
      color = input('Enter the color: ')
      rectangle(t, length, width, color)
      
   elif ask == 'circle':
      radius = int(input('Enter the radius: '))
      color = input('Enter the color: ')
      circle(t, radius, color)
      
   else:
      print('Wrong input, shape not available')
   ask = input('Pick a shape you want to draw: ').lower()