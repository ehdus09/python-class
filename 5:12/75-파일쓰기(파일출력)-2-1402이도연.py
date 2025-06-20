# 내용 표준입력받아 파일에 한 줄씩 쓰기, 내용 없으면 종료
f = open("data_3.txt", "w")

while True:
    content = input("내용 입력: ")

    if content != "":
        f.write(f'{content}\n')
    else:
        break

f.close()
print("정상종료")