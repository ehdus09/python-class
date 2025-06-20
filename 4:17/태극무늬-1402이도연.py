from turtle import *
shape("turtle")
bgcolor("black")
l = 1
speed(0)

for i in range(1, 501):
    if i % 3 == 1:
        color("red")
        fd(l)
        lt(119)
    elif i % 3 == 2:
        color("yellow")
        fd(l)
        lt(119)
    else:
        color("blue")
        fd(l)
        lt(119)
    l += 2



exitonclick()