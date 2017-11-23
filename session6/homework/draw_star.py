from turtle import *

def draw_star(x, y, length):
    penup()
    goto(x, y)
    for i in range(5):
        pendown()
        forward(length)
        penup()
        right(144)
    pendown()

# draw_star(0,0,100)
# mainloop()

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

# random.randint tạo ra 1 giá trị ngẫu nhiên cho tọa độ và kích thước của từng ngôi sao. 
