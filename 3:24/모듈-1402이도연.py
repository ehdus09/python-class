import calendar as cal
print(cal.prmonth(2025,3))

'''
r.rnadom() 0<=실수<1
r.uniform(a, b)a<=실수<b
r.randint(a, b)a<=정수<=b
r.randrange(a, b, step)a<=정수<b step간격으로 생성(리스트)
r.choice(리스트/문자열) 한 개 랜덤 추출 *데이터 자체 추출*
r.choices(리스트/문자열, k=숫자) k개 랜덤추출(중복허용) *리스트 형태 추출*
r.sample(리스트/문자열, k=숫자) k개 랜덤추출 *리스트 형태* (중복X)
ex)[1,2,3,4] 이럴 때 choices는 k =5일때 나왔던 값이 또 나옴. sample은 에러
r.shuffle(리스트/문자열) 리스트, 문자열 등의 요소 섞기(순서변경)
'''