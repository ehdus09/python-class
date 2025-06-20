import random as r
import time

easy = ['cat', 'dog', 'sun', 'car', 'cup', 'bat', 'box', 'map', 'pen', 'run']
normal = ['monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf', 'tiger', 'jungle']
hard = ['elephant', 'chocolate', 'university', 'dictionary', 'adventure', 'kangaroo', 'technology']


level = input("난이도 선택 (1: 쉬움 / 2: 보통 / 3: 어려움): ")
if level == '1':
    w = easy
elif level == '2':
    w = normal
elif level == '3':
    w = hard
else:
    print("잘못된 입력입니다. 기본 난이도(보통)으로 진행합니다.")
    w = normal

cnt = 0 # 맞은 개수
tries = 0 # 시도 횟수
t_count = 0 # 입력한 글자 수

input("\n[타자게임] 준비되면 엔터")
start = time.time()

i = 1
while cnt < 7:
    print(f'\n[문제 {i}]')
    q = r.choice(w)
    print(q)
    ans = input()

    tries += 1
    t_count += len(ans)

    if ans == q:
        cnt += 1
        print("pass")
        w.remove(q)
        i += 1
    else:
        print("fail")

end = time.time()
re = end - start

accuracy = (cnt / tries) * 100
speed = (t_count / re) * 60

# 결과 출력
print("\n 결과")
print(f'타자 시간: {re:.2f}초')
print(f'정확도: {accuracy:.1f}%')
print(f'타자 속도: {speed:.1f} 타/분')