import random as r


while True:
    a = r.randint(1,10)
    b = r.randint(1,10)
    
    if a == b:
        print(f'{a} ~ {b} => {a}')
        break
    else:
        total = 0
        # if a < b:
        #     for i in range(a, b + 1):
        #         total += i
        #     print(f'{a} ~ {b} => {total}')
        # else:
        #     for i in range(b, a + 1):
        #         total += i
        #     print(f'{b} ~ {a} => {total}')

        if a > b:
            a, b = b, a
        for i in range(a, b + 1):
            total += i
        print(f'{a} ~ {b} => {total}')
