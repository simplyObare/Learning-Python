from turtle import *

def square(t, size):
   for i in range(4):
      t.forward(size)
      t.left(90)
      
def triangle(t, size):
   for i in range(3):
      t.forward(size)
      t.left(120)
      
t = Turtle()
      
square(t, 100)

t.penup()
t.goto(-150, -50)
t.pendown()
triangle(t, 100)

done()