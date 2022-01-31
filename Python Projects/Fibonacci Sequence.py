# Introduction
print("\033[1;36m=-"*20, "\033[m")
print(f'\033[1;36m {"Fibonacci Sequence!":^40}\033[m')
print("\033[1;36m=-"*20, "\033[m")

#The user will type how any terms they want to see
number_terms = int(input("How many terms do you want to see?"))

#We set the 2 first terms, once there's no other way to have them 
first = 0
second = 1

#The counter will count how many terms is left to be printed. It will decrease by 2 because the terms will be printed in couples
for counter in range(number_terms, 0, -2):
    print(first, end=" --> ")
    if counter != 1: print(second, end=" --> ") #If there was only 1 term left to be printed when this loop started, the previous line will be executed, showing the last term, but this one won't, otherwise it would show more terms than it should.

    #"reserve" will reserve the "first" term value, then "first" will receive the sum of its antecessor, "second", with "reserve", that saved the old "first" value.
    reserve = first
    first = reserve + second

    #Now, "reserve" will receive the "second" term value, then "second" will receive the sum of its antecessor, "first"(formed in the previous lines), with "reserve", that saved the old "second" value
    reserve = second
    second = first + reserve
    #Now the "first" and "second" values will be printed, and the cycle will continue until the required quantity of terms shows up.

#After that, the code ends.
print("OK!")
print(f"Bye, bye! I'll miss you <3")
print("\033[1;34;107mBy: Kaique Apolinário\033[m")