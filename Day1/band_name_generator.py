#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
#2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew up in? ")
#3. Ask the user for the name of a pet.
ans = input("Do you have a pet?[y|n] ")
if ans == "y":
    pet = input("What's his or her name? ") 
else:
    pet = "no_pet"
#4. Combine the name of their city and pet and show them their band name.
print("The band " + "May day" + " grew up in " + city + " and has a pet named " + "'"+pet+"'")
# FIXME: skip to print name of a pet if they don't have a pet
# print("The band " + "May day" + " grew up in " + city + " and has a pet named " + pet if ans == "y" else "")

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end