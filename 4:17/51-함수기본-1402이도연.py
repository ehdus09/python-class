#51-1
def fun_s(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

#51-2
def fun_fact(n):
    mult = 1
    for i in range(1, n+1):
        mult *= i
    return mult

#main
print(fun_s(10))
print(fun_s(100))
print(fun_s(1000))

print(fun_fact(5))
print(fun_fact(10))