# Introduction
print("\033[1;36m=-"*20, "\033[m")
print(f'\033[1;36m {"Multiplication Table!":^40}\033[m')
print("\033[1;36m=-"*20, "\033[m")

# Verify if the input is a valid float or integer number
while True:
    while True:
        try:
            number = float(input("Type a number to see its times table: (Type 0 to end) "))
        except:
            print("Ooops! You should write a valid number.")
        else:
            break

# Stop the code if it's the number 0 and print the multiplication table
    if number != 0:
        for times in range (1, 11):
            print(number, "x", times, "=", number * times)
    else:
        break
print("See you soon!")
print("\033[1;34;107mBy: Kaique Apolinário\033[m")