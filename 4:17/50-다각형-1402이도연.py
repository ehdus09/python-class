from turtle import *
n = int(input("몇 각형: "))
outsideAngle = 360 / n

length = int(input("한 변의 길이: "))
shape("turtle")
color("yellowgreen")
fillcolor("skyblue")
pensize(10)

begin_fill()
for i in range(n):
    fd(length)
    lt(outsideAngle)
end_fill()

exitonclick()