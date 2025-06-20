while True:
    try:
        n = int(input())
    except ValueError:
        break
    else:
        if n % 5 == 0:
            print("5의 배수")
        else:
            print("5의 배수 아님")
        # if n % 5 == 0:
        #     print("5의 배수")
        #     continue
        #print("5의 배수 아님")