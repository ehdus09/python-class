#리스트 생성 함수 정의
def lst_create():
    print("*** 리스트 생성")
    lst = list(map(float, input("숫자(공백으로 분리): ").split()))
    return lst


#데이터 추가 함수 정의
def lst_append(lst):
    print("*** 숫자 추가(문자 입력 시 추가 종료)")
    while True:
        try:
            n = float(input('추가 숫자: '))
        except ValueError:
            break
        else:
            lst.append(n)
    return lst


#합계, 평균 계산 함수 정의
def lst_cal(lst):
    lstSum = sum(lst)
    lstAvg = lstSum / len(lst)
    return lstSum, lstAvg #합계, 평균을 튜플 형태로 반환


#출력함수 호출
def lst_print(lst, result):
    print("*** 계산 결과")
    print(f'점수: {lst}')
    print(f'합계: {result[0]:.2f} 평균: {result[1]:.2f}')


#main
lst = lst_create()

lst = lst_append(lst)

result = lst_cal(lst)
lst_print(lst, result)