sen = input("영문자열 입력: ").lower()
con_c, vow_c = 0, 0
vow = 'aeiou'
for i in sen:
    if not ('a' <= i <= 'z'): #i.isalpha() 알파벳인지 아닌지를 T/F로 알려줌 if else문 사용가능, isdigit - 숫자, isspace - 공백
        continue
    elif i in vow:
        vow_c += 1
    else:
        con_c += 1
print(f'자음: {con_c}개, 모음: {vow_c}개')