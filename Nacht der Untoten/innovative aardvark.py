#This is the beta testing script

vegan = input("Is there a vegan? (y/n): ").lower()
veg = input("Is there a vegetarian? (y/n): ").lower()
gluten = input("Is there a gluten sensitive person? (y/n): ").lower()

CONSTANT = ("Corner Cafe\nThe Chef's Kitchen")

print("\n" * 10)

if veg == "y" and gluten == "y" and vegan == "y":
    food = CONSTANT
    print("You can safely eat at the following places")
    print(food)
elif veg == "y" and gluten == "y" and vegan == "n":
    food = (CONSTANT + "\nMain Street Pizza Company")
    print("You can safely eat at the following places")
    print(food)
elif veg == "y" and gluten == "n" and vegan == "n":
    food = (CONSTANT + "\nMain Street Pizza Company\nMama's Fine Italian")
    print("You can safely eat at the following places")
    print(food)
elif veg == "y" and gluten == "n" and vegan == "y":
    food = CONSTANT
    print("You can safely eat at the following places")
    print(food)
elif veg == "n" and gluten == "y" and vegan == "y":
    food = CONSTANT
    print("You can safely eat at the following places")
    print(food)
elif veg == "n" and gluten == "n" and vegan == "y":
    food = CONSTANT
    print("You can safely eat at the following places")
    print(food)
elif veg == "n" and gluten == "y" and vegan == "n":
    food = (CONSTANT + "\nMain Street Pizza Company")
    print("You can safely eat at the following places")
    print(food)
else:
    food = (CONSTANT + "\nMain Street Pizza Company\nMama's Fine Italian\nJoe's Gourmet Burgers")
    print("You can safely eat anywhere. Here is a fun list.")
    print(food)