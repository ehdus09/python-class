#44-1
# row = int(input("행 수: "))
# col = int(input("열 수: "))
# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         print(f'{i * j:2}', end=" ")
#     print()


#44-2
row = int(input("행 수: "))
col = int(input("열 수: "))
# a = 1
# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         print(f'{(a + j)-1:2}', end=" ") #관계식((i-1) * col) + j
#     a += col
#     print()


#44-2-2
cnt = 1
for i in range(1, row+1):
    for i in range(1, col+1):
        print(cnt, end=" ")
        cnt+=1
    print()