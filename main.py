# input() will get user input in console

# Then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name? ") + "!")

# Then print() will print the word "Hello" and the user input
print(len(input("What is your name? ")))

# The following statement will have TypeError: can only concatenate str (not "int") to str
# How to correct? 
# print("Hello" + len(input("What is your name? ")) + "!")