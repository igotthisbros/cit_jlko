from turtle import *

# forward(300)
# left(120)
# forward(300)
# left(120)
# forward(300)
# done()
# sides = int (input("Type the number of sides : "))
# angle = 360/sides
# while sides > 0:
#     forward(300)
#     left(120)
#     sides -= 1

def rect(x, y, w, h, color):
    fillcolor(color)
    begin_fill()
    penup()
    goto(x,y)
    pendown()
    count = 2
    while count > 0:
        forward(w)
        left(90)
        forward(h)
        left(90)
        count -= 1
    end_fill()

rect(100, 100, 200, 300, 'black')
rect(-50, -100, 50, 200, 'darksalmon')
rect(50, -200, 30, 90, 'salmon')
done()
