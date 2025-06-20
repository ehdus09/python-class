f = int(input("과일 무게(g): "))

if f >= 375 or f < 210:
    print('"판정 불가"')
elif f < 250:
    print('"보통"')
elif f < 300:
    print('"상"')
elif f < 375:
    print('"특"')