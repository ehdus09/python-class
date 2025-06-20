fruit = []
while len(fruit) < 5:
    a = input()
    if a in fruit:
        print("이미 있음")
        continue
    fruit.append(a)
print(fruit)