from turtle import *
shape("turtle")
color("blue")
fillcolor("yellow")

up()
goto(-200, 200)
down()
begin_fill()
for i in range(4):
    fd(100)
    lt(90)
end_fill()

color("orange")
up()
goto(100, 100)
down()
for i in range(3):
    fd(100)
    lt(120)

exitonclick()