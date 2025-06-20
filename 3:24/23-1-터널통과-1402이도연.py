tunnel1, tunnel2, tunnel3 = map(int, input().split())
car = 170
if car <  tunnel1 and car < tunnel2 and car < tunnel3:
    print("pass")
else:
    print("crash")