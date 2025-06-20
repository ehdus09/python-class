import random as r
# user, computer 둘 다 숫자로 가위, 바위, 보 선택
rsp = int(input("입력(1.가위 2.바위 3.보): "))
case = {1:'가위', 2:'바위', 3:'보'}
c = r.randint(1, 3)

if c == rsp:
    result = '비겼음'
elif rsp - c == 1 or rsp - c == -2:
    result = '이겼음'
else:
    result = '졌음'

print(f'user: {case[rsp]} com: {case[c]} -> {result}')