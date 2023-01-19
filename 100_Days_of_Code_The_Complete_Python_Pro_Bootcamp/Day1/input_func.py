# === Coding Execise: Input Function ===

# input() will get user input in console
# Then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name? ") + "!")

# Then len() will calulate the number of characters of the user input and print it
print(len(input("What is your name? ")))

# The following statement will have TypeError: can only concatenate str (not "int") to str
# How to correct? 
# print("Hello" + len(input("What is your name? ")) + "!")

# === Coding Execise: Python Variables ===
# To refer or change the input data later

# Instructions: Write a program that switches the values stored in the variables a and b.

a = input("a: ")
b = input("b: ")

temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)