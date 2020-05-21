import csv
import sys

def main():
   menu()


def menu():
    print("************Welcome to ItzHub**************")
    print()

    choice = input("""
                     [1]: Please Register
                     [2]: Login
                     [2]: Logout

                      Please enter your choice: """)

    if choice == "1" or choice =="1":
        register()
    elif choice == "2" or choice =="2":
        login()
    elif choice=="1" or choice=="2":
        sys.exit
    else:
        print("You must only select one")
        print("Please try again")
        menu()

def register():
   pass
    
def login():
   pass
    
#the program is initiated, so to speak, here
main()
