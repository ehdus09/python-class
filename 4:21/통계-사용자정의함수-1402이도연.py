import math

#입력
def f_input():
    lst = list(map(int, input().split()))
    return lst


#평균
def f_avg(lst):
    mean = sum(lst)/len(lst)
    return mean


#분산
def f_var(lst):
    mean = f_avg(lst)
    vsum = 0
    for i in lst:
        vsum += (i-mean)**2
        var = vsum / len(lst)
    return var


#표준편차
def f_std(lst):
    var = f_var(lst)
    std = math.sqrt(var)
    return std


#최대공약수, 최소공배수
def f_common(lst):
    gcd = math.gcd(*lst)
    lcm = math.lcm(*lst)
    return(gcd, lcm) #여려개 리턴할 경우 튜플로 묶여 나옴


#main
lst = f_input()
print(lst)

print(f_avg(lst))

print(f_var(lst))

print(f_std(lst))

print(f_avg(lst))

print(f_common(lst))



