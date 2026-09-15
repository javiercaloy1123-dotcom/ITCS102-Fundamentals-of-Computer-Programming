print("==========LOAN EXPRESS=========")

age = int(input("Type Age: "))
is_employed = input("Are You Employed? (Type True or False): ")
has_collateral = input("Do you have Collateral? (Type True or False): ")
credit_score = int(input("Credit Score: "))
annual_income = int(input("Income: "))

print("\n========EVALUATING========\n")

if age < 21 or is_employed == "False":
    print("Result: Rejected: Fails baseline criteria")
else:
    if credit_score >= 750:
        if annual_income >= 100000:
            print("Result: Approved at 4.5% interest")
        else:
            print("Result: Approved at 5.0% interest")
            
    elif credit_score >= 600 and credit_score < 750:
        if has_collateral == "True":
            print("Result: Approved at 7.0% interest")
        elif annual_income < 40000:
            print("Result: Approved at 9.5% interest")
        else: 
            print("Result: Approved at 8.0% interest")
            
    else:
        print("Result: Rejected: Credit Score too low")

print("\n========RESULT========\n")
print(" Age:", age)
print(" Employed:", is_employed)
print(" Credit Score:", credit_score)
print(" Annual Income:", annual_income)
print(" Has Collateral:", has_collateral)