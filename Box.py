Square = 15
for a in range(Square):
  for b in range(Square):
    if a == Square - 1 or a == 0 or b == Square - 1 or b == 0:
      print("*", end=" ")
    else:
      print(" ", end=" ")  
  print()