# 한 행씩 읽어서 모두 출력
# readline()

f = open("data_2.txt", "r")

while True:
    line = f.readline()
    if line == "":
        break
    print(line.strip())

f.close()
