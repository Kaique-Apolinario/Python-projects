from random import sample
from time import sleep

# Introduction
print("\033[1;36m=-"*25, "\033[m")
print(f'\033[1;36m {"Area calculator(w/ BLACKPINK homage)!":^50}\033[m')
print("\033[1;36m=-"*25, "\033[m")

# Function to calculate the area of the rooms


def area(measures):
    return measures[0] * measures[1]

# Function to "draw" the rooms


def draw(bp):
    if homage in "[E]" and bp == 'IS':
        print("-"*20)
        print(f"|{'BLACKPINK':^18}|")
        print("-"*20)
    else:
        print("-" * 20)
        print(f"|{' ROOM ':^18}|")
        print("-" * 20)


room = 0
while True:
    while True:
        # This is just a silly play with BLACKPINK's (Girl Group that I like) catchphrase "BLACKPINK in your area!". Please, don't take it too seriously.
        # Here's the code to enable and disable the homage:
        homage = input(
            "First, enable or disable the BLACKPINK's homage? [D] for 'Disable' and [E] for 'Enable': ").upper().strip()
        if homage in "[E]" or homage in "[e]" or homage in "[d]" or homage in "[D]":
            break
        else:
            print("What? Try again!")
    room += 1

    # Type only numbers to be the room's measures
    while True:
        try:
            len_wid = [float(input(f"Type the length of the room {room}: ")), float(
                input("Now, the width: "))]
        except:
            print("Oops! You should type numbers. Try again!")
        else:
            break

    # Random the existence of BP in the room
    area(len_wid)
    bp = ''.join(sample(['IS', 'is NOT'], 1))
    print(
        "~~~~Let me see if BLACKPINK's in your area" if homage in "[E]" or homage in "[e]" else "",  end='')
    for wait in range(0, 6):
        sleep(1)
        print(".", end='')
    print(f"\nThe room's area is {area(len_wid):.2f}m²",
          end='' f" and BLACKPINK {bp} in your area, look:\n" if homage in "[E]" or homage in "[e]" else ", look:\n")
    draw(bp)

# Possibility to register new rooms
    while True:
        choice = input("Do you want to continue? [Y/N]").strip()
        if choice in "[Y]" or choice in "[y]" or choice in "[N]" or choice in "[n]":
            break
        else:
            print("What? Try again!")
    if choice in "[N]" or choice in "[n]":
        break
print("Bye, bye!")
print("\033[1;34;107mBy: Kaique Apolinário\033[m")
