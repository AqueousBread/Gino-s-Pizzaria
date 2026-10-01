#This is the beta testing script

vegan = input("Is there a vegan? (y/n): ").lower()
veg = input("Is there a vegetarian? (y/n): ").lower()
gluten = input("Is there a gluten sensitive person? (y/n): ").lower()

CONSTANT = ("Corner Cafe\nThe Chef's Kitchen")

print("\n" * 10)

if veg == "y" and gluten == "y" and vegan == "n":
    food = (CONSTANT + "\nMain Street Pizza Company")
elif veg == "y" and gluten == "n" and vegan == "n":
    food = (CONSTANT + "\nMain Street Pizza Company\nMama's Fine Italian")
elif veg == "n" and gluten == "n" and vegan == "n":
    food = (CONSTANT + "\nMain Street Pizza Company\nMama's Fine Italian\nJoe's Gourmet Burgers")
elif veg == "n" and gluten == "y" and vegan == "n":
    food = (CONSTANT + "\nMain Street Pizza Company")
else:
    food = CONSTANT


print("You can safely eat at the following places")
print(food)