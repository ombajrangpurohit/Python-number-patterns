rows = 5
k = 1
for i in range(rows):
    for j in range(rows):
        if i >= j:
            print(k, end = " ")
            k += 1
        else:
            print(" ", end = " ")
    print()