Sender_Name = input("    ENTER NAME.....>>")
Type_of_Package = input("    TYPE OF PACKAGE.....>>")
Is_Fragile = input("    FRAGILE...TRUE/FALSE...>>") == "TRUE"
Package_Weight = float(input("    ENTER WEIGHT.......>>"))
Distance_Kilometers = float(input("    ENTER DISTANCE KM.....>>"))
Is_Express = input("   Express?.. TRUE/FALSE.......>>") == "TRUE"
Is_International = input("   International?.....TRUE/FALSE....>>") == "TRUE"

base_cost = (Package_Weight * 2.50) + (Distance_Kilometers * 0.15)

if Package_Weight <= 2.0 and Distance_Kilometers <= 100 and not Is_Express and not Is_International:
    Total_Cost = 0

elif Is_International and Is_Express:
    Total_Cost = (base_cost * 1.40) + 50

elif Is_Express or (Is_International and Package_Weight > 20):
    Total_Cost = (base_cost * 1.20) + 25

elif Package_Weight > 30 or Distance_Kilometers > 1000:
    Total_Cost = base_cost + 30

else:
    Total_Cost = base_cost

print("Total cost is: PHP", Total_Cost)