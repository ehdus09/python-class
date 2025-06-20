# 사용자로부터 이름, 나이, 학교 입력받아 me.txt에 저장
name = input('이름: ')
age = input('나이: ')
school = input('학교: ')

# f = open("me.txt", "w")
# f.write(f'{name}\n{age}\n{school}')
# f.close()

with open('me.txt', "w") as f:
    f.write(f'이름: {name}\n')
    f.write(f'나이: {age}\n')
    f.write(f'학교: {school}\n')
# close안써도됨