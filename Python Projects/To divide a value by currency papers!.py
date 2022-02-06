#Introduction
print("\033[1;36m=-"*20, "\033[m")
print(f'\033[1;36m {"Dividing a value by currency papers!":^39}\033[m')
print("\033[1;36m=-"*20, "\033[m")

#Input of the value
money = int(input("Type the value of the money you want to take: "))
c1000 = c50 = c20 = c10 = c1 = 0

#How many notes of each currency paper you need to take
while money >= 1000:
    money -= 1000
    c1000 += 1
while money >= 50:
    money -= 50
    c50 += 1
while money >= 20:
    money -= 20
    c20 += 1
while money >= 10:
    money -= 10
    c10 += 1
while money >= 1:
    money -= 1
    c1 += 1
print(f"To take R${money}, you need to take: {c1000} currency papers of R$1000\n{c50} currency papers of R$50\n{c20} currency papers of R$20\n{c10} currency papers of R$10\n{c1} currency papers of R$1")
print("\033[1;34;107mBy: Kaique Apolinário\033[m")