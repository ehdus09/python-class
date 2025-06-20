from turtle import *
import random as r

# x, y 좌표범위
x_min, x_max = -5, 5
y_min, y_max = -5, 5

#그래프 간격
space = 0.1

#함수리스트
func_list = ["x*x", "abs(x)", "0.5*x + 1", "x*x*x + x*x*x + x*x + 1"]

#사용자 정의 좌표 설정, 거북 속도, 선 굵기
setworldcoordinates(x_min, y_min, x_max, y_max)
shape('turtle')
speed(0)
pensize(3)

#x축, y 그리기
up(); goto(x_min, 0)
down(); goto(x_max, 0)

up(); goto(0, y_min)
down(); goto(0, y_max)

colors = ['green','red','blue','purple']
#그래프 그리기
for func in func_list:
    col = r.choice(colors)
    color(col)
    colors.remove(col)
    x = x_min
    y = eval(func) #문자로 적은 수식을 알아서 계산해줌
    up()
    goto(x, y)
    down()
    
    #x_max까지 그래프 그리기
    while x <= x_max:
        x += space
        y = eval(func)
        goto(x, y)