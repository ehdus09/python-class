while True:
    n = int(input())
    if n == 0:
        break
    elif n % 5 == 0:
        print("5의 배수")
    else:
        print("5의 배수 아님")