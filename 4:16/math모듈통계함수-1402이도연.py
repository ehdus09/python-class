import math
lst = list(map(int, input().split()))
# lst = list(range(1, 11))
print(lst)

#평균
mean = sum(lst)/len(lst)
print(f'평균: {mean}')

#분산 (평균으로부터 얼마나 떨어져 있는지)
vsum = 0
for i in lst:
    vsum += (i-mean)**2
    var = vsum / len(lst)
print(f'분산: {var}')

#표준편차
#연산자이용 std = var ** (1/2)
std = math.sqrt(var)
print(f'표준편차: {std}')

#최대공약수, 최소공배수
gcd = math.gcd(*lst)
lcm = math.lcm(*lst)
# 가변길이 리스트를 인자(함수에 넘겨주는거)로 사용할 때 * 사용
print(f'최대공약수: {gcd} 최소공배수: {lcm}')