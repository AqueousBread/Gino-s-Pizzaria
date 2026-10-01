#Bingo Program
#
#version Beta.03 Hampter Edition
#9/28/26 Update: Added color and loop
#9/30/26 Update: Added array and check

#might need to explain import random and colorama

import random
from colorama import Fore, Back, Style, init
init(autoreset=True)

#creating the array
Numbers_Called = []


#time to pick a number
input("Press Enter to draw a bingo ball!")
Number = random.randint(1, 75)

#Number = int(input("Enter The Number (1 - 75): "))
#NEED TO CHANGE IT TO WHERE THE OUTPUT IS A VARIABLE SO THAT I CAN ADD IT TO THE ARRAY
if Number > 75 or Number < 1:
    print("The Number must be between 1 and 75")
    #Eventually Loop Back To Ask Again
elif Number >= 1 and Number < 15:
    Number = ("B", Number)
elif Number >=16  and Number < 30:
    Number = ("I", Number)
elif Number >= 31 and Number < 45:
    Number = ("N", Number)
elif Number >= 46 and Number < 60:
    Number = ("G", Number)
else:
    Number = ("O", Number)

print(Back.GREEN + Fore.LIGHTWHITE_EX + f"{Number}")
#attempting to add to the array
Numbers_Called.append(Number)

BingoCalled = input("Has Anyone Called Bingo? (y/n): ").lower()

if BingoCalled == "y":
    print(Back.LIGHTWHITE_EX + Fore.RED + "Come on up!")
else:
    if BingoCalled != "y" and BingoCalled != "n":
        print("Please enter either 'y' or 'n' next time.")
    print("We need to pick another number.....")
    while BingoCalled != "y":
        # time to pick a number
        input("Press Enter to draw a bingo ball!")
        Number = random.randint(1, 75)

        # Number = int(input("Enter The Number (1 - 75): "))
        if Number > 75 or Number < 1:
            print("The Number must be between 1 and 75")
            # Eventually Loop Back To Ask Again
        elif Number >= 1 and Number < 15:
            Number = ("B", Number)
        elif Number >= 16 and Number < 30:
            Number = ("I", Number)
        elif Number >= 31 and Number < 45:
            Number = ("N", Number)
        elif Number >= 46 and Number < 60:
            Number = ("G", Number)
        else:
            Number = ("O", Number)

        print(Back.GREEN + Fore.LIGHTWHITE_EX + f"{Number}")
        # attempting to add to the array
        Numbers_Called.append(Number)

        BingoCalled = input("Has Anyone Called Bingo? (y/n): ").lower()
        if BingoCalled != "y" and BingoCalled != "n":
            print("Please enter either 'y' or 'n' next time.")
        if BingoCalled == "y":
            print("Come on up!")
init(autoreset=False)
print("\n" * 5)
print(Back.BLACK + Fore.LIGHTWHITE_EX + "\t" + Back.LIGHTYELLOW_EX + Fore.BLACK + "\t{Numbers_Called}\t" + Back.BLACK + Fore.LIGHTWHITE_EX + "\t")
print(Back.LIGHTYELLOW_EX + Fore.LIGHTYELLOW_EX + "\t                 \t\t\t")
print(*Numbers_Called, sep="\n")