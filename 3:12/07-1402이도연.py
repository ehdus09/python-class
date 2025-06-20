#분초 계산 프로그램
print("#" * 20)
print(" 분초 계산 프로그램")
print("#" * 20)
sec = int(input("초 입력: "))
min = sec // 60
sec %= 60
print(f'결과: {min}분 {sec}초')