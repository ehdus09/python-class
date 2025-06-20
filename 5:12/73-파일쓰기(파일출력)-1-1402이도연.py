# 파일 없는거 적으면 만들어짐
# 바로쓰기
f = open("data_1.txt","w") # 경로지정안하면 파일이 이 코드저장되어있는 폴더와 같은 폴더에 만들어짐
f.write("안녕하세요\n") # write는 줄바꿈 포함X

# 표준입력 받아 쓰기
content = input()
f.write(f'{content}\n')
f.close()