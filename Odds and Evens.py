import random
from time import sleep


# Introduction
print("\033[1;36m=-"*20, "\033[m")
print(f'\033[1;36m {"Lets play Odds or Evens!":^40}\033[m')
print("\033[1;36m=-"*20, "\033[m")
name = input("Hello, I'm Kaique! You are?...").title()
print(f"{name}? Beautiful name! Let's play it: ")

while True:
    # Deciding who got evens and who got odds.
    pc = random.choice(['EVENS', 'ODDS'])
    if pc == "EVENS":
        user = "ODDS"
    else:
        user = "EVENS"
    print(f"I chose {pc}, so you're {user}!")

    # Choosing numbers and result
    pcnumber = random.randint(1, 10)
    usernumber = int(input("Okay! Now, you choose a number: "))
    result = pcnumber + usernumber

    # Who win the game and the end of it
    print("Hm.. Let me sum our numbers... I'm not good at math...")
    sleep(4.5)
    if pc == "EVENS" and result % 2 == 0:
        print(f"\033[1;31;107mAhaa! I chose {pcnumber} and you {usernumber}, thus, the sum is {result}, a EVEN number, so YOU LOSE!!! :D\033[m")
    elif pc == "ODDS" and result % 2 != 0:
        print(f"\033[1;31;107mAhaa! I chose {pcnumber} and you {usernumber}, thus, the sum is {result}, a ODD number, so YOU LOSE!!! :D\033[m")
    elif user == "EVENS" and result % 2 == 0:
        print(f"\033[1;32;107mNoo! I chose {pcnumber} and you {usernumber}, thus, the sum is {result}, a EVEN number, so YOU WIN!!! :(\033[m")
    elif user == "ODDS" and result % 2 != 0:
        print(f"\033[1;32;107mNoo! I chose {pcnumber} and you {usernumber}, thus, the sum is {result}, a ODD number, so YOU WIN!!! :(\033[m")

    # Endgame
    print(f"That was fun!", end=' ')
    while True:
        choice = input("Do you want to play again? [Y]/[N] \n").upper()
        if choice in "[Y][N]":
            break
        else:
            print("I didn't understand your answer!", end=" ")
    if choice in "[N]":
        break
print(f"Bye, bye, {name}! I'll miss you <3")

