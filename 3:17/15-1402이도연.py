stu1 = {'학반':105, '번호':20, '이름':'홍길동'}
print(stu1['학반']) #키로 값 찾기
print(stu1['번호'])
print(stu1['이름'])
print(stu1.get('이름')) # 키로 값에 접근
#두 개의 차이점: get은 없는 키를 찾았을 때 None이 나오고, get없는건 없는 키를 찾았을 때 에러/get은 함수니까 뒤에 ()
print(stu1.get('주소'))
#print(stu1['주소'])
#딕셔너리의 키를 리스트로 만들고 싶을 때
print(stu1.keys()) #딕셔너리의 모든 키 반환
print(list(stu1.keys()))
#딕셔너리의 값을 리스트로 만들고 싶을 때
print(stu1.values()) #딕셔너리의 모든 값 반환
print(list(stu1.values()))
print('이름' in stu1) #딕셔너리 안에 키가 있는지 확인 / 리스트에도 쓰임, 조건문 만들 때 많이 쓰임
print('주소' in stu1)