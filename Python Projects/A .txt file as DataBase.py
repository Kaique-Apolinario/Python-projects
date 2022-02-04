from time import sleep
from sys import exit

def dec(msg):
    print("=-"*20)
    print(f"{msg:^40}")
    print("=-"*20)


def menu():
    while True:
        dec("MENU")
        #If the user doesn't choose a option, they will get stuck in a loop.
        choice = input("1- Register a person\n2- See the list\n3- Exit\n")
        if choice.isnumeric() and choice in ("1", "2", "3"):
            break
        else:
            print("ERROR: You typed a wrong number. Try again!")
    return int(choice)

# Introduction
print("\033[1;36m=-"*20, "\033[m")
print(f'\033[1;36m {"A .txt file as DataBase!":^40}\033[m')
print("\033[1;36m=-"*20, "\033[m")


while True:

    #The user will choose what they want to do with it
    choice = menu()

    #If the user chooses to "Register a person"
    if choice == 1:
        dec("REGISTER") #The introduction
        
        #The name they want to register
        name = input("Name:").strip().title()
        while True:

            #They age of the person the user want to register; The user have to type a integer number, else, they will get stuck in a loop
            age = input("Age:")
            if not age.isnumeric():
               print("Type a valid age, please. ")
            else:
                break
        
        #A "DataBase.txt" is created (if it doesn't exist in the user machine) and allow to read and write in it. The "DataBase" variable receives the file.
        DataBase = open("DataBase", "a+")

        #The name and age typed are written inside the file
        DataBase.write(f"{name:<18} {age:>9} years old\n")

        #The document is closed
        DataBase.close()

    #If the user chooses to "See the list"
    elif choice == 2:
        dec("LIST") #The introduction

    #If the user tries to see the list but it's empty, a warning will tell that is is empty, else, the list will be showed normally
        try:
            DataBase = open("DataBase", "r") #It will open the "DataBase.txt" and allow to read it, so the "DataBase" variable will receive it
        except:
            print("Oops! There's no name registered in the list yet!\n"), sleep(3)
        else:    
            print(DataBase.read().rstrip())    
            DataBase.close()

    #If the user choose to "Exit" the programm
    elif choice == 3:
        print(f"Try to come back and the name will still be in the list!"), sleep(3)
        print(f"Bye, bye! I'll miss you <3")
        print("\033[1;34;107mBy: Kaique Apolinário\033[m")
        exit()


