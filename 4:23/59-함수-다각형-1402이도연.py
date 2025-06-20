from turtle import *

#한 변의 길이와 도형 종류 입력
def input_data():
    while True:
        a, b = map(int, input('종류(3이상) 한 변 (5이상): ').split())
        if a >= 3 and b >= 5:
            return a, b
        else:
            print('조건에 맞게 다시 입력해주세요')
            continue

#이동함수
def moving():
    x, y = map(int, input('이동할 좌표(x, y): ').split())
    up()
    goto(x, y)
    down()
    

#도형그리기
def polygon():
    n, a = input_data()
    for i in range(n):
        fd(a)
        lt(360 / n)
        
        
# 색깔과 도형 바꾸기
def change_color_shape():
    col, shap = input('색과 포인터 입력: ').split()
    color(col)
    shape(shap)


#메인
print("===도형 그리기===")
while True:
    chan = int(input('색, 도형 바꾸기(1) 안바꾸기(그 외): '))
    if chan == 1:
        change_color_shape()
    moving()
    polygon()

    con = int(input('계속(1) 중단(그 외): '))
    if con != 1:
        break
    
exitonclick()