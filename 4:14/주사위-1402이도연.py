for i in range(1, 7):
    for j in range(1, 7):
        print(f'({i}, {j})',end=" ")
    print()

print()

for i in range(1, 7):
    for j in range(1, 7):
        print(f'({j}, {i})',end=" ")
    print()

print()

for i in range(1, 7):
    for j in range(1, 7):
        if i == j:
            print("      ", end=" ")
            continue
        print(f'({j}, {i})',end=" ")
    print()