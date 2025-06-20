#영어, 숫자, 공백, 특수문자
n, space, special,vow, con = 0, 0, 0, 0, 0
vow = 'aeiou'
sen = input()
for i in sen:
    if i.isalpha():
        if i in vow:
            vow += 1
        else:
            con += 1
    elif i.isdigit:
        n += 1
    elif i.isspace():
        space += 1
    else:
        special += 1
print(f'모음 {vow}개, 자음 {con}개, 숫자 {n}개, 공백 {space}개, 특수문자 {special}개')