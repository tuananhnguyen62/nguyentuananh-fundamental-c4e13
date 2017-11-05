colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *
speed(-10)
c = -1
for i in range(3, 8):
    c += 1
    pencolor = colors[c]
    color(pencolor)
    for j in range(i):
        forward(100)
        left(360/i)

mainloop()
