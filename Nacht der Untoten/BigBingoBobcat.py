#This is for generating a bingo board.
#The current idea to explore is using a grid coordinate system where the first B-O is for BINGO,
#and the second B-0 is the vertical coordinate.
#IN Example. A grid would look like as follows
#     B  I  N  G  O
#   B
#   I
#   N
#   G
#   O
#There was an attempt with 0-4, but it didn't like having numbers as variables.


#Started 9/30/26
#Bingo Board: Big Bingo Bobcat (B5)
    #changelog: Now adding the win mechanics


#all imports
import random
from colorama import init, Fore, Back, Style
init(autoreset=True)
import json


#creating variables for the coords and giving them random numbers accordingly (code may or may not be just copied from
#the PAP Hampter program.)

#select a mode
WinCon = input("What is your win condition: Cover, Diag, Vert, Horiz, or any? ").lower()

User = input("What is your username: ").upper()
GamesWon = 0
data = {"User": User, "GamesWon": GamesWon, active=True}
with open("user_data.json", "w", encoding="utf-8") as f:





#ISSUE: ( SOLVED ) REPEAT NUMBERS (HOW TO PREVENT THAT? probably manual checks)
BB = random.randint(1, 15)
BI = random.randint(1, 15)
while BI == BB:
    BI = random.randint(1, 15)
BN = random.randint(1, 15)
while BN == BB or BI == BN:
    BN = random.randint(1, 15)
BG = random.randint(1, 15)
while BG == BB or BG == BN or BI == BG:
    BG = random.randint(1, 15)
BO = random.randint(1, 15)
while BO == BB or BO == BN or BO == BG or BI == BO:
    BO = random.randint(1, 15)

print("\n" * 5)
print("B section")
print(BB)
print(BI)
print(BN)
print(BG)
print(BO)

#fixing formatting to make 1 digit numbers into 2 digit numbers.

if BB < 10: BB = f"{BB:02d}"
if BI < 10: BI = f"{BI:02d}"
if BN < 10: BN = f"{BN:02d}"
if BG < 10: BG = f"{BG:02d}"
if BO < 10: BO = f"{BO:02d}"



IB = random.randint(16, 30)
II = random.randint(16, 30)
while IB == II:
    II = random.randint(16, 30)
IN = random.randint(16, 30)
while IB == IN or II == IN:
    IN = random.randint(16, 30)
IG = random.randint(16, 30)
while IB == IG or II == IG or IN == IG:
    IG = random.randint(16, 30)
IO = random.randint(16, 30)
while IB == IO or II == IO or IN == IO or IG == IO:
    IO = random.randint(16, 30)

print("\n" * 5)
print("I section")
print(IB)
print(II)
print(IN)
print(IG)
print(IO)


NB = random.randint(31, 45)
NI = random.randint(31, 45)
while NB == NI:
    NI = random.randint(31, 45)
NN = ("**")
NG = random.randint(31, 45)
while NB == NG or NI == NG or NN == NG:
    IG = random.randint(31, 45)
NO = random.randint(31, 45)
while NB == NO or NI == NO or NN == NO or NG == NO:
    NO = random.randint(31, 45)

print("\n" * 5)
print("N section")
print(NB)
print(NI)
print(NN)
print(NG)
print(NO)


GB = random.randint(46, 60)
GI = random.randint(46, 60)
while GB == GI:
    GI = random.randint(46, 60)
GN = random.randint(46, 60)
while GB == GN or GI == GN:
    GN = random.randint(46, 60)
GG = random.randint(46, 60)
while GB == GG or GI == GG or GN == GG:
    GG = random.randint(46, 60)
GO = random.randint(46, 60)
while GB == GO or GI == GO or GN == GO or GG == GO:
    GO = random.randint(46, 60)

print("\n" * 5)
print("G section")
print(GB)
print(GI)
print(GN)
print(GG)
print(GO)


OB = random.randint(61, 75)
OI = random.randint(61, 75)
while OB == OI:
    OI = random.randint(61, 75)
ON = random.randint(61, 75)
while OB == ON or OI == ON:
    ON = random.randint(61, 75)
OG = random.randint(61, 75)
while OB == OG or OI == OG or ON == OG:
    OG = random.randint(61, 75)
OO = random.randint(61, 75)
while OB == OO or OI == OO or ON == OO or OG == OO:
    OO = random.randint(61, 75)

print("\n" * 5)
print("O section")
print(OB)
print(OI)
print(ON)
print(OG)
print(OO)


print("\n" * 5)

#two spaces between each letter
print(Back.LIGHTWHITE_EX + Fore.BLACK + "B    I    N    G    O ")
print(Back.WHITE + Fore.BLACK + f'{BB} | {IB} | {NB} | {GB} | {OB}')
print(Back.WHITE + Fore.BLACK + f'{BI} | {II} | {NI} | {GI} | {OI}')
print(Back.WHITE + Fore.BLACK + f'{BN} | {IN} | {NN} | {GN} | {ON}')
print(Back.WHITE + Fore.BLACK + f'{BG} | {IG} | {NG} | {GG} | {OG}')
print(Back.WHITE + Fore.BLACK + f'{BO} | {IO} | {NO} | {GO} | {OO}')

#print(" B    I    N    G    O\n", BB, "|", IB, "|", NB, "|", GB, "|", OB, "\n", BI, "|", II, "|", NI, "|", GI, "|", OI, "\n", BN, "|", IN, "|", NN, "|", GN, "|", ON, "\n", BG, "|", IG, "|", NG, "|", GG, "|", OG, "\n", BO, "|", IO, "|", NO, "|", GO, "|", OO)
#the above was deemed unnessicary due to the board being still visible in the program from earlier.


#Now time for us to add the checker

Bingo = False

while Bingo == False:
    numCalled = input("What number was called? (Not the letter) If the number is less than 10, please put a 0 in front.: ")

    fixVariable = "10"
    if numCalled >= fixVariable: numCalled = int(numCalled)

    #if BB < 10: BB = f"{BB:02d}"

    #currently only works for the B column
    if numCalled == BB:
        BB = "**"
    elif numCalled == IB:
        IB = "**"
    elif numCalled == NB:
        NB = "**"
    elif numCalled == GB:
        GB = "**"
    elif numCalled == OB:
        OB = "**"
    elif numCalled == BI:
        BI = "**"
    elif numCalled == II:
        II = "**"
    elif numCalled == NI:
        NI = "**"
    elif numCalled == GI:
        GI = "**"
    elif numCalled == OI:
        OI = "**"
    elif numCalled == BN:
        BN = "**"
    elif numCalled == IN:
        IN = "**"
    elif numCalled == GN:
        GN = "**"
    elif numCalled == ON:
        ON = "**"
    elif numCalled == BG:
        BG = "**"
    elif numCalled == IG:
        IG = "**"
    elif numCalled == NG:
        NG = "**"
    elif numCalled == GG:
        GG = "**"
    elif numCalled == OG:
        OG = "**"
    elif numCalled == BO:
        BO = "**"
    elif numCalled == IO:
        IO = "**"
    elif numCalled == NO:
        NO = "**"
    elif numCalled == GO:
        GO = "**"
    elif numCalled == OO:
        OO = "**"
    else: print("Sorry, It's not on your card, or you didn't put a 0 in front.")

    print(Back.LIGHTWHITE_EX + Fore.BLACK + "B    I    N    G    O ")
    print(Back.WHITE + Fore.BLACK + f'{BB} | {IB} | {NB} | {GB} | {OB}')
    print(Back.WHITE + Fore.BLACK + f'{BI} | {II} | {NI} | {GI} | {OI}')
    print(Back.WHITE + Fore.BLACK + f'{BN} | {IN} | {NN} | {GN} | {ON}')
    print(Back.WHITE + Fore.BLACK + f'{BG} | {IG} | {NG} | {GG} | {OG}')
    print(Back.WHITE + Fore.BLACK + f'{BO} | {IO} | {NO} | {GO} | {OO}')

    if WinCon == "cover" and BB == "**" and IB == "**" and NB == "**" and GB == "**" and OB == "**" and BI == "**" and II == "**" and NI == "**" and GI == "**" and OI == "**" and BN == "**" and IN == "**" and NN == "**" and GN == "**" and ON == "**" and BG == "**" and IG == "**" and NG == "**" and GG == "**" and OG == "**" and BO == "**" and IO == "**" and NO == "**" and GO == "**" and OO == "**":
        print("BINGO! CALL IT OUT!")
        Bingo = True

    if WinCon == "diag":
        if BB == "**" and II == "**" and NN == "**" and GG == "**" and OO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BO == "**" and IG == "**" and NN == "**" and GI == "**" and OB == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True

    if WinCon == "vert":
        if BB == "**" and BI == "**" and BN == "**" and BG == "**" and BO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if IB == "**" and II == "**" and IN == "**" and IG == "**" and IO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if NB == "**" and NI == "**" and NN == "**" and NG == "**" and NO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if GB == "**" and GI == "**" and GN == "**" and GG == "**" and GO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if OB == "**" and OI == "**" and ON == "**" and OG == "**" and OO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True

    if WinCon == "horiz":
        if BB == "**" and IB == "**" and NB == "**" and GB == "**" and OB == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BI == "**" and II == "**" and NI == "**" and GI == "**" and OI == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BN == "**" and IN == "**" and NN == "**" and GN == "**" and ON == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BG == "**" and IG == "**" and NG == "**" and GG == "**" and OG == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BO == "**" and IO == "**" and NO == "**" and GO == "**" and OO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
    if WinCon == "any":
        if BB == "**" and IB == "**" and NB == "**" and GB == "**" and OB == "**" and BI == "**" and II == "**" and NI == "**" and GI == "**" and OI == "**" and BN == "**" and IN == "**" and NN == "**" and GN == "**" and ON == "**" and BG == "**" and IG == "**" and NG == "**" and GG == "**" and OG == "**" and BO == "**" and IO == "**" and NO == "**" and GO == "**" and OO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BB == "**" and II == "**" and NN == "**" and GG == "**" and OO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BO == "**" and IG == "**" and NN == "**" and GI == "**" and OB == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BB == "**" and BI == "**" and BN == "**" and BG == "**" and BO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if IB == "**" and II == "**" and IN == "**" and IG == "**" and IO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if NB == "**" and NI == "**" and NN == "**" and NG == "**" and NO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if GB == "**" and GI == "**" and GN == "**" and GG == "**" and GO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if OB == "**" and OI == "**" and ON == "**" and OG == "**" and OO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BB == "**" and IB == "**" and NB == "**" and GB == "**" and OB == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BI == "**" and II == "**" and NI == "**" and GI == "**" and OI == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BN == "**" and IN == "**" and NN == "**" and GN == "**" and ON == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BG == "**" and IG == "**" and NG == "**" and GG == "**" and OG == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True
        if BO == "**" and IO == "**" and NO == "**" and GO == "**" and OO == "**":
            print("BINGO! CALL IT OUT!")
            Bingo = True