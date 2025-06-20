#두 개의 점을 지나는 직선의 방정식
#두 점 입력
def get_data():
    a1, b1 = map(int, input("(x1, y1): ").split(","))
    a2, b2 = map(int, input("(x2, y2): ").split(","))
    return a1, b1, a2, b2


#기울기, y절편
def get_line(a1, b1, a2, b2):
    if a1 == a2:
        result = f'x = {a1}'
    else:
        slp = (b2 - b1) / (a2 - a1)
        y_i = b1 - slp * a1
        result = f'y = {slp}x + ({y_i})'
    return result
#main
x1, y1, x2, y2 = get_data()
line = get_line(x1, y1, x2, y2)
print(line)