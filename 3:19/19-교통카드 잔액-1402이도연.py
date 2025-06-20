# 방법 1
fee = 850
card = int(input("카드 잔액: "))

if card >= fee:
    print('탑승 가능')
else:
    print('탑승 불가능')

# 방법 2
fee = 850
card = int(input("카드 잔액: "))

if card < fee:
    print('탑승 불가능')
else:
    print('탑승 가능')