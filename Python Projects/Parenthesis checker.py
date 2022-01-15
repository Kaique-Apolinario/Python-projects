from time import sleep
#Introduction
print("\033[1;36m=-"*20, "\033[m")
print(f'\033[1;36m {"Parenthesis Checker!":^40}\033[m')
print("\033[1;36m=-"*20, "\033[m")

while True:
    #Type a equation with parenthesis
    while True:
        equation = input("Type a equation with parentheses: ")
        if ")" not in equation or "(" not in equation:
            print("Didn't find a '(' or ')'.", end=" ")
        else:
            break

    print(f"{equation}? Hm... let me see it...")
    sleep(2.5)
    calculation = 0
    #This will analyze each caractere looking for a parentheses
    for caractere in equation:

        #Calculation will receive +1 every time it finds a '(' and will lose -1 when it finds a ')' 
        #Calculation needs to end up with 0 points, which would mean every '(' has its corresponding ')', once the +1 point given by '(' will be annulated by the -1 point of ')'.
        if caractere == "(":
            calculation += 1
        
        elif caractere == ")":
            calculation -= 1
        
        #If the calculation be below 0, it means that it has ')' without its '(', so the programm knows it's a invalid equation.
        if calculation < 0:
            break

    # If the calculation be above 0, it means that has '(' without its ')', so the programm knows it's a invalid equation.
    if calculation == 0:
        print("It IS a valid equation! ")
    else:
        print("It's NOT a valid equation!")
    print("=-"*20)
    while True:
        choice = input("Do you want to try it again? [Y]/[N]\n").upper()
        if choice in "[Y]" or choice in "[N]":
            break
        else:
            print("Sorry, I don't understand.", end=' ')
    if choice in "[N]":
        break
print("Bye, bye! I hope you liked it! :)")
print("\033[1;34;107mBy: Kaique Apolinário\033[m")