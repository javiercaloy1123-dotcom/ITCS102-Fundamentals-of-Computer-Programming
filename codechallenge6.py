size = 50
for x in range(size):
    for y in range(size):
        if x == y or x + y == size - 1:
            print("*", end="")
        else:
            print(" ", end="")     
    print() 