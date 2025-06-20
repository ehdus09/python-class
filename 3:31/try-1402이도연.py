# #예외처리
# a = 4
# b = 0
# try:
#     c = a / b
# except ZeroDivisionError:
#     pass
while True:
    try:
        n_1 = int(input('숫자: '))
    except ValueError:
        print('숫자을 입력하세요.')
        #밑에 코드 더 있을 때 위로 가고 싶으면 continue
    else:
        print(n_1)
        break #반복문 빠져나가기