import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ made with codes ]+]+]+')
    print(bcolors.GREEN + '''
	                    
						
                      ItzHub
   
                                       Author: ItzDxniel
*.______________________________________________________________,'
                                                                 ''')

def main(start):

choice ='0'
while choice =='0':
    print(b.colors.RED + '\n+[+[+[ Main Choice: Choose 1 of 5 choices ]+]+]')
    print("Choose 1 for something")
    print("Choose 2 for something")
    print("Choose 3 for something")
    print("Choose 4 for something")
    print("Choose 5 to go to another menu")

    choice = input ("Please make a choice: ")

    if choice == "5":
        print("Go to another menu")
        second_menu()
    elif choice == "4":
        print("Do Something 4")
    elif choice == "3":
        print("Do Something 3")
    elif choice == "2":
        print("Do Something 2")
    elif choice == "1":
        print("Do Something 1")
    else:
        print("I don't understand your choice.")

 def second_menu():
     print("This is the second menu")

 main()
			
