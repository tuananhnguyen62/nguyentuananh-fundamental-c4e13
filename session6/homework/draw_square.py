from turtle import *

shape("turtle")

def draw_square(length, turtle_color):
    speed(-1)
    color(turtle_color)
    for i in range(4):
        forward(length)
        left(90)

# draw_square(100,'Blue')
# mainloop()

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()
