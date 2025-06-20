juice = 5
price = 800

while True:
    print("="*20)
    money = int(input("돈을 넣어주세요: "))
    
    if money > price:
        change = money - price
        print(f'맛있는 주스 드시고 잔돈 {change}원 받아 가세요.')
        juice -= 1
    elif money == price:
        print('맛있는 주스 드세요.')
        juice -= 1
    else:
        print(f'가격을 확인하세요.\n{money}')

    if juice == 0:
        print("주스가 매진되었습니다.")
        break