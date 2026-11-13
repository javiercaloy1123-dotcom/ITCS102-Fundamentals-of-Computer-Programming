#TASK 1
# loan 
amo = float(input("Enter the loan amount: "))
yrs = int(input("Enter the loan period in years: "))

# calculations
months = yrs * 12
princ = amo / months
bal = amo

# Output headers
print("\nPayment Schedule")
print("Month\t|   Monthly Payment\t|   Interest\t\t|   Principal\t\t|   Remaining Loan")
print("-" * 85) 

for a in range(1, months + 1):
    interest = bal * 0.0025
    payment = princ + interest
    bal = bal - princ

    if bal < 0.005:
        bal = 0
        
    print(f"{a}\t\t|   {payment:.2f}\t\t\t|   {interest:.2f}\t\t\t|   {princ:.2f}\t\t\t|   {bal:.2f}")


print("-" * 85)

 

#TASK2

for z in range(15):
    for y in range(15):
        if z + y == 7 or y - z == 7 or z == 8:
            print("+", end="") 
        else:
            print(" ", end="") 
    print()




#TASK3

for z in range(6):
    for y in range(6):
        if z == 0 or y + z == 5 or z == 5: 
            print("*", end="")
        else:
            print(" ", end="")
    print()