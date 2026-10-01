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
#Bingo Board Bobcat (B3)


#all imports
import random

#creating variables for the coords and giving them random numbers accordingly (code may or may not be just copied from
#the PAP Hampter program.)

#ISSUE: REPEAT NUMBERS (HOW TO PREVENT THAT? probably manual checks
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
NN = random.randint(31, 45)
while NB == NN or NI == NN:
    IN = random.randint(31, 45)
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