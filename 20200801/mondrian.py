from turtle import *
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

rect(0, 0, 300, 300, 'white')
rect(-300, 0, 300, 300, 'darkorange')
rect(0, -30, 300, 100, 'white')
rect(-300, -30, 300, 100, 'white')
rect(0, -250, 170, 250,'blue')
rect(0, -300, 170, 20, 'white')
done()
