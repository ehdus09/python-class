
aa = [10, 20, 30, 40]
print(aa[0:3])
print(aa[2:4])
print(aa[2:]) #[2:1] 거꾸로 쓰면 빈리스트 나옴 우와 대박신박해
print(aa[:2])

bb = [10, 20, 30]
cc = [40, 50, 60]
print(bb + cc) #계산 X 문자처럼 연결되서 나옴
print(bb * 2)

r = range(1,10, 1)
print(r)
a = list(range(10))
print(a)

#홀수(1~100), 짝수 (1~100)
odd = list(range(1, 101, 2))
even = list(range(2, 101, 2))

print(len(odd))
print(even.index(66))
print(even.count(66))

#list.append(데이터) 추가 리스트 제일 뒤에 데이터 추가, 위치 지정 X
#list.insert(인덱스, 데이터) 지정된 위치에 데이터 삽입, 위치 지정
#list a.extend(list b) 리스트 뒤에 다른 리스트 추가 연산자 + 느낌, 하지만 +는 저장하려면 변수 저장해야함. extend는 list바뀜
#list.remove(data) 특정 데이터 삭제
#del list[index] 해당 인덱스의 항목 삭제, 함수아님 명령어, 그냥 삭제
#list.pop() 리스트의 마지막데이터 추출, 인덱스 적으면 그 인덱스 삭제 후 저장, 변수 필요
