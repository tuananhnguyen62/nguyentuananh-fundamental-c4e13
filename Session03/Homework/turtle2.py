colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *
speed(-10)
c = -1
for i in range(len(colors)):
    c += 1
    pen_color = colors[c]
    color(pen_color)
    begin_fill()
    for j in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)
    forward(100)
    end_fill()

mainloop()
