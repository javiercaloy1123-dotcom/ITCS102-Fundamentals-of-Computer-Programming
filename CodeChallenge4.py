import getpass

print("==========LOAN EXPRESS=========")
username = "Carlo Javier"
password = "mahalko123"

b = input("  LOGIN USERNAME ==>> ")
a = getpass.getpass("  PASSWORD ==>> ")

#  username AND password must be correct
if b == username and a == password:
    print("!!!access granted!!!\n")
    
    # --- INPUT SECTION ---
    age = int(input("Input age: "))
    job_description = input("Type Job: ")
    salary_amount = float(input("Type Salary Amount: Php "))
    
    is_employed = input("Are you currently employed (True/False): ")
    
    credit_score = int(input("Credit Score: "))
    annual_income = float(input("What is your annual income: "))
    
    has_collateral = input("Do you have any collateral (True/False): ")
  
    collateral_type = "None"
    collateral_value = 0.0
    
    if has_collateral == "True":
       
        collateral_type = input("Enter Collateral Type (e.g. motorcycle, land, house): ")
        collateral_value = float(input("Enter the value of the collateral: Php "))

    loan_amount = float(input("Enter amount to loan: Php "))

    print("\n========EVALUATING========")

    # --- EVALUATION ---
    final_rate = 0.0
    is_approved = False
    
    if age < 21 or age > 65 or is_employed == "False":
        print("Result: Rejected (Age must be 21-65 and employed)")
        
    elif has_collateral == "True" and collateral_value < 30000:
        print("Result: Rejected (Collateral value must be at least Php 30,000)")
        
    else:
        # Credit Score approval
        if credit_score >= 750:
            if annual_income >= 100000:
                final_rate = 0.045
            else:
                final_rate = 0.05
            is_approved = True
            
        elif credit_score >= 600:
            if has_collateral == "True":
                final_rate = 0.07
            elif annual_income < 40000:
                final_rate = 0.095
            else:
                final_rate = 0.08
            is_approved = True
            
        else:
            print("Result: Rejected (Credit Score too low)")

    if is_approved == True:
        calculated_interest = loan_amount * final_rate
        print("Result: Approved at", final_rate * 100, "% interest.")
        print("Calculated Interest: Php", calculated_interest)

    # --- RESULT SECTION ---
    print("\n========RESULT========")
    print("Username:", username)
    print("Age:", age)
    print("Employed:", is_employed)
    print("Job Description:", job_description)
    print("Salary: Php", salary_amount)
    print("Credit Score:", credit_score)
    print("Annual Income: Php", annual_income)
    print("Loan Amount: Php", loan_amount)
    print("Has Collateral:", has_collateral)
    
    if has_collateral == "True":
      
        print("Collateral Type:", collateral_type)
        print("Collateral Value: Php", collateral_value)

else:
    print("!!!access denied!!!")