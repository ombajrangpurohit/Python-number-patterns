rows = 5
for i in range(rows):
    for j in range(rows):
        if j >= i:
            print(i + 1, end=" ")
        else:   
            print(" ", end = " ")
    print()