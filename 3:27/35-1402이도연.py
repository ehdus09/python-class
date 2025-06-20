#1개씩 카운팅
hap = 0
count = 0
while True:
    score = float(input())
    if score < 0:
        break
    hap += score
    count += 1
avg = hap / count
print(f'{avg:.1f}')

#리스트
score = []
while True:
    s = float(input())
    if s < 0:
        break
    score.append(s)
avg = sum(score) / len(score)
print(f'{avg:.1f}')