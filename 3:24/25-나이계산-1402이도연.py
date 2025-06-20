birth, gender = input().split(",")
gender = int(gender)
year = 2025
birth_year = int(birth[:2])
'''년도만 빼기: 문자열 인덱싱, 10000으로 나눈 몫'''
if gender % 2 == 0:
    gen = "여성"
else:
    gen = "남성"
if gender < 3:
    age = year - (birth_year + 1900) + 1
    print(f'현재나이 {age}살 {gen}입니다.')
else:
    age = year - (birth_year + 2000) + 1
    print(f'현재나이 {age}살 {gen}입니다.')