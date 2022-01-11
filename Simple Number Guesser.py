import random
from time import sleep

# Introduction
print("\033[1;36m=-"*20, "\033[m")
print(f'\033[1;36m {"Lets play Number Guesser!":^40}\033[m')
print("\033[1;36m=-"*20, "\033[m")
sleep(1)

while True:
    pc = random.randint(0, 5)
    while True:
        print("I chose a number between 0 and 5, try to guess it: ", end=' ')
        attempts = 0
        while True:
            try:
                chose = int(input())
                attempts += 1
            except:
                print("Oops! You should type a integer number! ", end=' ')
            else:
                if chose > 5 or chose < 0:
                    print("I told you to choose a number between 0 and 5 <3 ")
                    continue
                break


        while chose != pc:
            print("Oops!!! That was not the number I chose. Try again: ", end ='')
            while True:
                try:
                    chose = int(input())
                    attempts += 1
                except:
                    print("Oops! You should type a integer number! ", end=' ')
                else:
                    if chose > 5 or chose < 0:
                        print("I told you to choose a number between 0 and 5 <3 ")
                        continue
                    break
            
        print(f"Yes! you made it with {attempts} attempts!")
        while True:
            choice = input("Do you want to play again? [Y]/[N] \n").upper()
            if choice in "[Y][N]":
                break
            else:
                print("I didn't understand your answer!", end=" ")
        if choice in "[N]":
            break
        break
print(f"Bye, bye! I'll miss you <3")
print("\033[1;34;107mBy: Kaique Apolinário\033[m")