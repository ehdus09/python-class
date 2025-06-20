# 58-1 결과학인
def sub1(x):
    a = x + 100
    return a


def sub2(x):
    global a
    a = x + 100
    return a


#58-2 결과확인
def sub_1(lst):
    mylst = list(range(7, 11))
    print(f'sub_1 함수리스트: {mylst}')


def sub_2(lst):
    global mylst
    mylst = list(range(1, 5))
    print(f'sub_2 함수리스트: {mylst}')


#메인
a = 10
print(sub1(a)) # 110
print(a) # 10
print(sub2(a)) # 110
print(a) # 110, global때문에 함수 내 변수가 전체에 영향을 미침

mylst = list(range(10, 50, 10))
sub_1(mylst) # 넘겨 줬음에도 불구하고 함수안에서 재정의 되고, 지역변수라 7, 8, 9, 10
sub_2(mylst) # 1, 2, 3, 4 최종으로 정의 된게 1, 2, 3, 4
print(f'메인함수 리스트: {mylst}') # 1, 2, 3, 4 함수에 있던게 글로벌선언 되어서 main 함수 바뀜
#변수 헷갈리니까 이름 다르게, 글로벌로 쓰는건 같게 해도 ㄱㅊ