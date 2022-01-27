# Introduction
print("\033[1;36m=-"*20, "\033[m")
print(f'\033[1;36m {"Number Analyzer!":^40}\033[m')
print("\033[1;36m=-"*20, "\033[m")

while True:
    # If the user types anything but numbers, they'll get stuck in a loop.
    while True:
        try:
            numbers = {"Number1": int(
                input("Type 2 numbers: ")), "Number2": int(input())}
        except:
            print("You have to type 2 integer numbers.")
        else:
            break

    # Choices the user can make and its respective actions
    choice = int(input(
        "What you wanna do with these numbers?\n[1] Sum\n[2] Multiply\n[3] The bigger one\n[4] Change numbers\n[5] End of the programm\n"))
    if choice == 1:
        print(
            f"The sum between {numbers['Number1']} and {numbers['Number2']} is {numbers['Number1'] + numbers['Number2']}.")
    elif choice == 2:
        print(
            f"The multiplication of {numbers['Number1']} and {numbers['Number2']} is {numbers['Number1'] * numbers['Number2']}.")
    elif choice == 3:
        print(f"The biggest number typed is {max(numbers.values())}.")
    elif choice == 4:
        continue
    elif choice == 5:
        break
    while True:

        # If the player want to use it
        continuation = input("\nDo you want to continue? [S]/[N] ").upper()
        if (continuation in "[S]" or continuation in "[N]") and continuation not in "[]":
            break
        else:
            print("I didn't understand your choice.", end=' ')
    if continuation not in "[S]":
        break

# Goodbye
print(f"\nBye, bye! I'll miss you <3")
print("\033[1;34;107mBy: Kaique Apolinário\033[m")
