n = 7

center = n // 2

for z in range(n):
    for y in range(n):
      
        if z + y == center or y - z == center or z - y == center or z + y == n + center - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()