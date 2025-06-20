#오른쪽(0), 위쪽(90), 왼쪽(180), 아래쪽(270)
from turtle import *

d = 10
# 상하좌우 이동
def turn_right():
    setheading(0) ; fd(d)

def turn_up():
    setheading(90) ; fd(d)

def turn_left():
    setheading(180) ; fd(d)

def turn_down():
    setheading(270) ; fd(d)


# clear
def blank():
    clear()

#펜 토
pen_state = True

def toggle_pen():
    global pen_state
    if pen_state:
        up()
    else:
        down()
    pen_state = not pen_state
    listen()

#키보드
def keyboard():
    shape("turtle")
    speed(0)
    pensize(5)
    onkeypress(turn_right, "Right")
    onkeypress(turn_up, "Up")
    onkeypress(turn_left, "Left")
    onkeypress(turn_down, "Down")
    onkeypress(blank, "Escape")
    onkeypress(toggle_pen, "space")
    listen()
    
    
#마우스
def mouse():
    shape("turtle")
    speed(0)
    pensize(5)
    ondrag(goto)
    ondrag(blank, "Escape")
    listen()
    


#main
select = input("키보드(1) 마우스(2): ")
if select == "1":
    keyboard()
elif select == "2":
    mouse()