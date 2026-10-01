#Bingo Program
#
#version .01

Number = int(input("Enter The Number (1 - 75): "))
if Number > 75 or Number < 1:
    print("The Number must be between 1 and 75")
    #Eventually Loop Back To Ask Again
elif Number >= 1 and Number < 15:
    print(f"B{Number}")
elif Number >=16  and Number < 30:
    print(f"I{Number}")
elif Number >= 31 and Number < 45:
    print(f"N{Number}")
elif Number >= 46 and Number < 60:
    print(f"G{Number}")
else:
    print(f"O{Number}")

BingoCalled = input("Has Anyone Called Bingo?: ")

if BingoCalled == "Yes":
    print("Come on up!")
else:
    print("We need to pick another number.....")
    #Loop Back To Input