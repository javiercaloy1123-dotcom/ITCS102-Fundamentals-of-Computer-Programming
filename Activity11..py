#Login/Logout/Acesss

import getpass

username = "Carlo Javier"
password = "mahalko123"

b = input("Input USERNAME==>>")
a = getpass.getpass("Input PASSWORD==>>")

if b == username or a == password:

       print("!!!access granted!!!")

else:
      print("!!!acess denied!!! ")
