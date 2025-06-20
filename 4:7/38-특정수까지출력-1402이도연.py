#38-1
n = int(input('어디까지 출력할까요?: '))
for i in range(1, n+1):
    print(i)

#i는 지역변수
#38-2
n = int(input('어디부터 출력할까요?: '))
for i in range(n, -1, -1):
    print(i)

#38-3
n = int(input('몇 단?: '))
for i in range(1, 10):
    print("{} * {} = {}".format(n, i, n * i))