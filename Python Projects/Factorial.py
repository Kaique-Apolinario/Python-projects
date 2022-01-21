# Introduction
print("\033[1;36m=-"*20, "\033[m")
print(f'\033[1;36m {"Factorial of numbers with For/While":^40}\033[m')
print("\033[1;36m=-"*20, "\033[m")

while True:
    while True:
        # If the user type anything but a integer number, they'll get stuck in a loop
        print("\nThis one's using 'for': ")  # That's the code using for
        try:
            number = int(input("Type a number: "))
        except:
            print("You have to type a integer number!", end=" ")
        else:
            break

    # The result will receive the number the user typed
    result = number

    # All that "result" has to do is to multiply itself with the "counter", that will decrease by 1 each loop, until it be 1
    for counter in range(number-1, 0, -1):
        # It will avoid something like "factor x factor x factor x product"
        print(counter+1, "x " if counter != 1 else "x 1 = ", end='')
        result *= counter
    print(result)  # It will print the result of the factorial

    while True:
        print("\nThis one's using 'while': ")  # That's the code using while
        # If the user type anything but a integer number, they'll get stuck in a loop
        try:
            initial_number = number = int(input("Type a number: "))
        except:
            print("You have to type a integer number!", end=" ")
        else:
            break

    # The result will now receive "1", beuca if it had received the number the user typed, they both would multiply and mess the result.
    result = 1

    # The number the user typed will decrease until it reach "1"
    while number > 0:
        # It will avoid something like "factor x factor x factor x product"
        print(number, "x " if number != 1 else "= ", end='')

        # The result will be multiplied by the number that will decrease each loop
        result *= number
        number -= 1
    # It'll avoid the result shows "1" when the user type 0, per exemple.
    print(result if initial_number > 0 else "This number has no factorial.")
    while True:

        # Possibility of play it again
        choice = input("Do you want to try it again? [Y]/[N]\n").upper()
        if choice in "[Y]" or choice in "[N]":
            break
        else:
            print("Sorry, I don't understand.", end=' ')
    if choice in "[N]":
        break

# Goodbye
print(f"\nBye, bye! I'll miss you <3")
print("\033[1;34;107mBy: Kaique Apolinário\033[m")
