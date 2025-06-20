import math
def createSen():
    a, b, c = map(int, input().split())
    return a, b, c

def D(a, b, c):
    d = b**2-4*a*c
    if d < 0:
        print("허근")
    else:
        return (-b + math.sqrt(d)) /2*a, (-b - math.sqrt(d)) /2*a

#main
a, b, c = createSen()
print(D(a, b, c)[0], D(a, b, c)[1])