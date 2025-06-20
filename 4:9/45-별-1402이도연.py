#1
r = int(input("행 수: "))
for i in range(1, r+1):
    for j in range(i):
        print("*", end="")
    print()

# for i in range(1, n+1):
#     for j in range(i):
#         print('*', end=" ")
#     print()

#2
r = int(input("행 수: "))
for i in range(r, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# for i in range(n, 0, -1):
#     for j in range(i):
#         print('*', end=" ")
#     print()

#3
r = int(input("행 수: "))
for i in range(1, r+1):
    for j in range(r-i): # 공백 띄우는 개수가 행수-그 행
        print(' ', end = " ")
    for j in range(i):
        print("*", end=" ")
    print()

# for i in range(1, n+1):
#     for j in range(n-i):
#         print(' ', end=" ")
#     for k in range(i):
#         print('*', end=" ")
#     print()

#4
r = int(input("행 수: "))
for i in range(r, 0, -1):
    for j in range(r-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()


#5
r = int(input("행 수: "))
for i in range(1, r + 1):
    for j in range(r - i):
        print(" ", end=" ")
    for j in range(i * 2 - 1):
        print("*", end=" ")
    print()