#Bingo Program
#
#version Beta.02 Hampter Edition
#9/28/26 Update: Added color and loop

#might need to explain import random and colorama

import random
from colorama import Fore, Back, Style, init
init(autoreset=True)

#time to pick a number
input("Press Enter to draw a bingo ball!")
Number = random.randint(1, 75)

#Number = int(input("Enter The Number (1 - 75): "))
if Number > 75 or Number < 1:
    print("The Number must be between 1 and 75")
    #Eventually Loop Back To Ask Again
elif Number >= 1 and Number < 15:
    print(Back.GREEN + Fore.LIGHTWHITE_EX + f"B {Number}")
elif Number >=16  and Number < 30:
    print(Back.GREEN + Fore.LIGHTWHITE_EX + f"I {Number}")
elif Number >= 31 and Number < 45:
    print(Back.GREEN + Fore.LIGHTWHITE_EX + f"N {Number}")
elif Number >= 46 and Number < 60:
    print(Back.GREEN + Fore.LIGHTWHITE_EX + f"G {Number}")
else:
    print(Back.GREEN + Fore.LIGHTWHITE_EX + f"O {Number}")

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
            print(Back.GREEN + Fore.LIGHTWHITE_EX + f"B {Number}")
        elif Number >= 16 and Number < 30:
            print(Back.GREEN + Fore.LIGHTWHITE_EX + f"I {Number}")
        elif Number >= 31 and Number < 45:
            print(Back.GREEN + Fore.LIGHTWHITE_EX + f"N {Number}")
        elif Number >= 46 and Number < 60:
            print(Back.GREEN + Fore.LIGHTWHITE_EX + f"G {Number}")
        else:
            print(Back.GREEN + Fore.LIGHTWHITE_EX + f"O {Number}")

        BingoCalled = input("Has Anyone Called Bingo? (y/n): ").lower()
        if BingoCalled != "y" and BingoCalled != "n":
            print("Please enter either 'y' or 'n' next time.")
        if BingoCalled == "y":
            print("Come on up!")