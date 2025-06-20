# 이름 여러 개 입력받아 attendance.txt에 한 줄 씩 저장
with open('attendance.txt', 'w') as f:
    for i in range(5):
        name = input(f'{i + 1}번: ')
        f.write(f'{name}\n')