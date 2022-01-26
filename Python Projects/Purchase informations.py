#Introduction
print("\033[1;36m=-"*20, "\033[m")
print(f'\033[1;36m {"Time to buy!":^40}\033[m')
print("\033[1;36m=-"*20, "\033[m")

# Type the product's name and how much it costs
total = cheapest = QuantityOfProducts = ProductsCust1000 = 0
while True:
    productname = str(input("Type here a product's name: "))
    while True:
        try:
            price = float(input("How much it costs? "))
        except:
            print("I don't understand you answer.", end=' ')
        else:
            break
        
    #Calculate the total price of the purchase
    total += price

    #Calculate how many products that cost more than R$1000 there is
    QuantityOfProducts += 1
    if price > 1000:
        ProductsCust1000 += 1

    #Calculate the cheapest product
    if QuantityOfProducts == 1 or cheapest > price:
        cheapest = price
        cheapestname = productname
            
    #Possibility of buying more
    while True:
        choice = input("Do you want to continue? [Y] or [N]? ").upper().strip()    
        if choice in "[Y]" or choice in "[N]":
            break
        else:
            print("I don't understand you answer.", end=' ')
    if choice in "[N]":
        break

#Purchase informations
print(f"The total expense is R${total}, and there's {ProductsCust1000} products that costs more than R$1000 meanwhile the cheapest product is {cheapestname} that costs R${cheapest}.")
print("\033[1;34;107mBy: Kaique Apolinário\033[m")