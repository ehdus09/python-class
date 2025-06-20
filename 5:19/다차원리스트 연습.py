'''
arr=[0 for i in range(3)]
for i in range(3):
    arr[i] = list(map(int, input().split()))
'''

arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))
    
print("결과확인")
for i in range(3):
    for j in range(3):
        print(arr[i][j], end=" ")
    print()