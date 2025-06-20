# 51-1 1~n까지의 합
#함수정의
def fun_s(n):
    if n<2:
        return 1
    else:
        return n + fun_s(n-1)


# 51-2 1~n까지의 곱
def fun_f(n):
    if n<2:
        return 1
    else:
        return n * fun_f(n-1)
    
#메인
print(fun_s(1))
print(fun_s(10))
a = int(input('자연수: '))
print(fun_s(a))


print(fun_f(1))
print(fun_f(10))
a = int(input('자연수: '))
print(fun_f(a))