import random as r
import time

cnt=0
w = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']

input("[타자게임] 준비되면 엔터")
start = time.time()
i = 1
while cnt < 5:
    print(f'[문제 {i}]')
    q = r.choice(w)
    print(q)
    ans = input()
    if ans == q:
        cnt += 1
        print("pass")
        i += 1
    else:
        print("fail")
end = time.time()
re = end - start
print(f'타자시간: {re}초')