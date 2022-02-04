from sys import exit
from time import sleep
import os

def dec(msg):
    print("\n"*2)
    print("=-"*20)
    print(f"{msg:^40}")
    print("=-"*20)


def menu():
    while True:
        dec("MENU")
        #If the user doesn't choose a option, they will get stuck in a loop.
        choice = input("1- Register a person\n2- See the list\n3- Delete Someone\n4- Exit\n").strip()
        if choice.isnumeric() and choice in ("1", "2", "3", "4"):
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
        while True:
            name = input("Name: ").strip().title()
            if name == "":
                print("Please, Type a Proper", end=" ")
                continue
            else: 
                break
        while True:

            #They age of the person the user want to register; The user have to type a integer number, else, they will get stuck in a loop
            age = input("Age: ").strip()
            if not age.isnumeric():
               print("Type a valid age, please. ")
            else:
                break
        
        #A "DataBase.txt" is created (if it doesn't exist in the user machine) and allow to read and write in it. The "DataBase" variable receives the file.
        DataBase = open("DataBase.txt", "a+")

        #The name and age typed are written inside the file
        DataBase.write(f"{name:<18} {age:>9} years old\n")

        #The document is closed
        DataBase.close()
        input("\033[4;33mPress Enter to continue:\033[m ")
        

    #If the user chooses to "See the list"
    elif choice == 2:
        dec("LIST") #The introduction

    #If the user tries to see the list but it's empty, a warning will tell that is is empty, else, the list will be showed normally
        try:
            DataBase = open("DataBase.txt", "r")
        finally:
            if os.stat("DataBase.txt").st_size == 0:
                print("Oops! There's no name registered in the list yet!\n")
            else:    
                print(DataBase.read().rstrip())    
        input("\033[4;33mPress Enter to continue:\033[m ")








    #If the user chooses to "Delete Someone"
    elif choice == 3:
        dec("DELETE") #The introduction

        try:
            DataBase = open("DataBase.txt", "r+") #It will open the "DataBase.txt" and allow to read it, so the "DataBase" variable will receive it
        finally:
            
            #If the user tries to see the list but it's empty, a warning will tell that is is empty, else, the list will be showed normally
            if os.stat("DataBase.txt").st_size == 0:
                print("Oops! There's no name registered in the list yet!\n")
                input("\033[4;33mPress Enter to continue:\033[m ")
            else:    
                ListOfLines = DataBase.readlines() #Here, each line from the "DataBase.txt" will be a string inside a list, so the "ListOfLines" var will receive this list

                #If the user tries to delete a line that doesn't exist, a warning will show up and the user will get stuck in a loop
                while True:
                    try:
                        LineToDelete = int(input(f"Type here the line you want to delete(from 1 to {len(ListOfLines)}): ")) 
                        if LineToDelete == 0: #If the user types "0", the code would delete the first line, but it shouldn't happen, because there isn't a "line 0"
                            raise SystemExit(0)
                        ListOfLines.pop(LineToDelete-1) #Here, the string that is at the position of the number that the user typed will be deleted of the "ListOfLines" var
                    except:
                        print("Oops! That line does not exist in the list!", end=' ')
                    else:
                        break    
                DataBase.truncate(0) #Here, the "DataBase.txt" content will be erased
                DataBase.write("".join(ListOfLines)) #Here, each line of "ListOfLines" var will be a line in "Database.txt" 
                DataBase.close()











    #If the user choose to "Exit" the programm
    elif choice == 4:
        print(f"\033[1;32mTry to come back and the name will still be in the list!\033[m")
        print(f"Bye, bye! I'll miss you <3")
        print("\033[1;34;107mBy: Kaique Apolinário\033[m")
        exit()


