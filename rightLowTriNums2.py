rows = 5
for i in range(rows):
    for j in range(rows):
        if j >= rows - i - 1:
            print(i + 1, end=" ")
        else:   
            print(" ", end = " ")
    print()