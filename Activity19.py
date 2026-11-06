from getpass import getpass
isCaloy = False
loginAttempt = 0

user = "Caloy1123"
password = "pogi123"

while isCaloy == False:
    name = input("type Name --->>")
    key = getpass("tpye Key--->>")

    if name == user and key == password:
        print("Access Granted")
        print("Total Login Attempts ", loginAttempt)
        isCaloy = True
    else:
        print("Acess Denied")
        loginAttempt += 1
        isCaloy = False
    