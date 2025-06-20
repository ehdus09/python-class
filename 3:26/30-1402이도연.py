num = 1
while num <= 10:
    print(f'현재숫자는 {num}')
print("프로그램 종료")

num = 1
while num <= 10:
    print(f'현재 숫자는 {num}')
    num += 1
print("프로그램 종료")

num = 1
while True:
    print(f'현재 숫자는 {num}')
    num += 1
    if num > 10:
        print('프로그램 종료')
        break #break뒤에 뭐 쓰면 안됨