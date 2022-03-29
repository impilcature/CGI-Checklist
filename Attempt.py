from src.cgilib.domain import models

def mainMenu():
    print("[1] Checklist Selection.")
    print("[2] Edit Checklist Components")

def componentMenu():
    print("[1] Edit Checklist")
    print("[2] Edit Person")
    print("[3] Edit Command")
    print("[4] Return to main menu")

mainMenu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        #Enter code here.
        print("option 1 selected")
        print()

    elif option == 2:
        #Enter code here.
        componentMenu()
        print()

    else:
        print("Invalid Option.")
        print()
    
    mainMenu()
    option = int(input("Enter your option: "))

    