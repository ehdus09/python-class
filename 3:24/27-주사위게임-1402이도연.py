import random as r

user = list(map(int, input("2개 입력(1~6, 중복허용): ").split()))
num = list(range(1, 7))
com = list(r.choices(num, k = 2))

if user[0] in com and user[1] in com:
    result = 1
elif user[0] in com or user[1] in com:
    result = 2
else:
    result = 3

print(f'Com={com} User={user} \n{result}등!')