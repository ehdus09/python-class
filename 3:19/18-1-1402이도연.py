a = int(input("score: "))

if a >= 80:
    print("A")
#elif 60 <= a <80:
elif a >= 60: # 위에 if에서 내려왔으면 이미 80보다 작다는거임
    print("B")
else:
    print("C")
print("END")