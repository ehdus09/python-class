#사각형
from turtle import *
shape("turtle")#글자는 따옴
color("green")
pensize(3) #숫자는 걍
speed(3)

for i in range(4):
    fd(100)
    lt(90)
    
#삼각형
color("yellow")
for i in range(3):
    fd(100)
    lt(120)

#원
color("orange")
circle(50)