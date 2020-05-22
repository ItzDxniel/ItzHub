import csv
import sys
import NitroGen
import bomber

def main():
   menu()


def menu():
    print("************Welcome to ItzHub**************")
    print()

    choice = input("""
                     [1]: Discord Nitro (Generator + Checker)
                     [2]: TBomb
                     [3]: Exit

                      Please enter your choice: """)

    if choice == "1" or choice =="1":
        register()
    elif choice == "2" or choice =="2":
        login()
    elif choice=="3" or choice=="3":
        sys.exit
    else:
        print("You must only select one")
        print("Please try again")
        menu()

def register():
   execfile('NitroGen.py'):
        
def login():
   execfile('bomber.py'):
    
#the program is initiated, so to speak, here
main()
