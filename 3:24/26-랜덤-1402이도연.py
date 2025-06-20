import random as r

#0이상 1미만 실수 중 난수
print(r.random())

#10이상 11미만 실수 중 난수
print(r.uniform(10, 11))

#10이상 100이하
print(r.randint(10, 100))

#10이상 100미만 10간격 정수
print(r.randrange(1, 100, 10))

#1이상 10미만 1간격 정수리스트 생성
a_list = list(range(1, 10))

#임의의 수 1개 출력
print(r.choice(a_list))

#3개 중복 허용
print(r.choices(a_list, k=3))

#2개 중복X
print(r.sample(a_list, k = 2))

teacher = ['마아람', '정다혜', '강진아', '이승호']
#리스트 요소의 순서 임의로 변경해 출력
r.shuffle(teacher) #print()안에 r.shuffle넣으면 None나옴
print(teacher)

#리스트에서 임의의 요소 출력
print(r.choice(teacher))