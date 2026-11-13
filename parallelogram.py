n = 7
r = 4
for z in range(r): 
    for y in range(n): 
        if z + y == r - 1 or (z == 0 and y >= 3):
            print("*", end="")
        elif (z == r - 1 and y <= 3) or (z + y == n - 1 and y >= 4):
            print("*", end="")
        else:
            print(" ", end="")
    print()