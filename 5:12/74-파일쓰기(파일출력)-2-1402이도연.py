# 반복문으로 한 줄씩 쓰기
f = open("data_2.txt", "w")
for i in range(1, 11):
    # line = input()
    line = f'{i}번째 줄\n'
    f.write(f'{line}\n')

f.close()
print("정상종료")