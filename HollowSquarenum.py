side = 5
for i in range(side):
    for j in range(side):
        if i == 0 or i == side - 1 or j == 0 or j == side - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()