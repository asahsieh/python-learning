# Variables
name = "Beau" # This is inline comment
print(name)

# Data type
print(type(name) == str)
print(isinstance(name, str)) # name is an instance of class str()

age = 2
print(isinstance(age, int))   # True
print(isinstance(age, float)) # False

## casting
age = float(2)
number = "20"
print(isinstance(number, int)) # False
age = int(number)
print(isinstance(age, int))    # True 
print() # Remove me if there has method to add newline to the previous statement

## Other types
complex
bool
list
tuple
range
dict
set

print("Operators")
# Operators
## Arithmetic Operators
1 + -1 # 0
4 ** 2 # 4 to the power of 2
4 // 2 # 2

print("Scramp" + " is a good dog")
age = 8
print(f"age = {age}")
age += 8
print(f"age += 8, age = {age}")
age *= 8
print(f"age *= 8, age = {age}")

## Comparison Operators
a = 1
b = 2

a == b # Output = False
a != b # True
a > b  # False
a <= b # True

## Boolean Operators
##
### 'or' using an expression returns the value of the first operand
### that is not a false value or a falsy value, otherwise it returns
### the last operand
print(0 or 1) # 1
print(False or 'hey') # 'hey' 
print('hi' or 'hey') # 'hi' 
print([] or False) # 'False' Both of empty list ([]) and False are false 
print(False or []) # '[]'    the last operand is return 

### 'and' only evaluate the second argument if the first one is true
print(0 and 1) # '0'
print('' and 'hey') # '': empty string

### Summary of 'or' and 'and': return the last operand if all operands are positive to the operator

## Bitwise operators
### ^ performs a binary XOR operation

## *** is & in Operators ***
### 'is' is called the identity operator
### it's used to compare two objects and returns true if both are the same objects  

### 'in' is called the membership operator
### this is used to tell if a value is contained in a list or another sequence

## Ternary operator
### The slow way
def is_adult(age):
    if (age) > 18:
        return True
    else:
        return False

### by the ternary operator
def is_adult2(age):
    return True if age > 18 else False

print(is_adult2(20))
print(is_adult2(18))

# Strings
"Beau"
name = "Beau"
phase = name + " is my name"
name += " is my name"
print(name + '.')

## Use str class constructor to make a number a string
age = str(39)

## A multi-line string: when the string is defined with a special syntax,
## enclosing the string in a set of three quotes
print("""Beau is

39

years olds
""")

## String Methods
print("beau".upper())

## isalpha() to check if string contains only characters and is not empty
## isalrum | () to check if a string contains characters or digits and is not empty
## isdecimal() to check if a string contains digits and is not
## empty
## lower() to get a lowercase version of a string
## islower() to check if a string is lowercase
## upper() to get an uppercase version of a string
## supper() to check if a string is uppercase
## title() to get a capitalized version of a string 
## startsswith) to check if the string starts with a specific substring

### HIGHLIGHT: one thing to know about these is that they all return a new modified string,
###            they don't actually alter the original string
name = "Beau"
print("name: " + name)
print(name)

print("name.lower(): ")
print(name.lower())

### You can use some global functions with strings as well
print("name.len(): ")
print(len(name))

### One use case on using the 'in' operator
### to check if a string contrains a substring 
print("\"au\" in name: ")
print("au" in name)

## Escaping Characters

## String Characters & Slicing
### you can get characters of a string using square brackets to
### get a specific item or 
### wrap around from the left most character to the right most character
print("name[-1]:")
print(name[-1]) # 'u' from "Beau"

#### a range what we call slicing
##### if you just put a blank before or after the colon
##### then it's going to turn everything from 
##### the left most character or the right most character
print("name[:8]")
print(name[:8]) # "Beau" 
print("name[1:]")
print(name[1:]) # "eau"

# Boolean
print("=== Boolean ===")
## bool type
done = True
done = False

if done:
    print("yes")
else:
    print("no")

## number 
## only 0 is False, others are True
done = -1 # yes 
done = 0  # no
print(f"done = {done} and is evaluated as boolean value: ")

if done:
    print("yes")
else:
    print("no")

## string
## only empty string ("") is False, others are True
done = "111" # yes 
done = ""    # no 
print(f"done = {done} and is evaluated as boolean value: ")

if done:
    print("yes")
else:
    print("no")

## check the value is a boolean
done = True
print(type(done) == bool)

done = "beau" 
print(type(done) == bool)

## apply global functions