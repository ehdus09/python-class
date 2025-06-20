#39-1
n = int(input("자연수입력: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print(f'1부터 {n}까지의 합은 {sum}')

#39-2
n = int(input("자연수입력: "))
mult = 1
for i in range(1, n+1):
    mult *= i
print(f'{n}!은 {mult}')