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
### any
book_1_read = True 
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
print(f"read_any_book = {read_any_book}")

### all
ingredients_purchased = True
meal_cooked = False 

ready_to_serve = all([ingredients_purchased, meal_cooked]);
print(f"ready_to_serve = {ready_to_serve}")

# Number Data Types
## complex
num1 = 2+3j
num2 = complex(2,3)

print(num2.real, num2.imag)
## built-in functions
### abs
num1 = -5.49
print(abs(num1))

### round
num1 = abs(num1)
print(round(num1))   
#### the second parameter is to set the decimal points precision 
print(round(5.49, 1)) # 5.5 
print(round(5.49, 2)) # 5.49

### enum: this is the only way to create constanst in python
print("\n=== enum ===")
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

#### get assigned value of state
print(State.ACTIVE.value)
print(State['ACTIVE'].value) # by square brackets
print("")

#### get state in string 
print(State.ACTIVE)
print(State(1))
print(State['ACTIVE']) # by square brackets

#### List all the possible values for enum
print("list(State), len(State)")
print(list(State), len(State))

### user inputs
default = 37
age = input("What is your age? ") or default
print(f"Your age is {age}")

# Lists: are essential python data structure
print("=== List ===")

## a list can hold different types of values
dogs = ["Roger", 1, "Syn", True] 

## check if an item is contained in a list with the "in operator"
print("Roger" in dogs) # True
print("Beau" in dogs)  # False

### False on empty list
dogs = []
print("Beau" in dogs)  # False

## Reference items in a list by their indexes starting with zero
dogs = ["Roger", 1, "Syn", True] 
print(dogs[0])
### update an item using the same notation
dogs[2] = "Beau"
print("Replace \"Syn\" to \"Beau\"")
print(dogs)
### you can also use negative number here
print("==== compare element ====")
print("Check whether the elements are the same on the index in positive and negative numbers:")
if dogs[2] == dogs[-1]: 
    print("The elements are the same:")
    print(dogs[2])
else: 
    print("The elements are different:")
    print(dogs[2])
    print(dogs[-1])
    
### slicing
print(dogs[1:3]) # the second number is upper bound; only dogs[1] and dogs[2] are printed 
print(dogs[0:])  # all elements are printed
print(dogs[:3])  # elements with index < 3 are printed

### Append
print("Append \"Judah\" into list")
print("Length of list is changed from")
print(len(dogs))
dogs.append("Judah")
print("to")
print(len(dogs))
print(dogs)

### Extend a list by adding more than one element
#### by the extend method
dogs.extend(["Quincy"])
dogs.extend([7])
print(dogs)
#### +=
dogs += ["Syd", 8]
print(dogs)
##### put characters of the string as elements if you miss bracket
dogs += "Syd"
print(dogs)

### Remove an item
#### by remove() method
dogs.remove("Syd")
print(dogs)
#### pop(): remove the last item from the list 
####        and it's going to return the last item
poped_item = dogs.pop()
print(poped_item)
print(dogs.pop())

### Add an item in the middle of the list by specific INDEX
items = ["Roger", 1, "Syn", True, "Quincy", 7] 
items.insert(2, "Test")
print(items)

#### Add multiple items by slice
##### insert elements FROM position 1
items[1:1] = ["Test1", "Test2"]
print(items)

##### the list of elements will be treated as an element 
items[1] = ["Test1", "Test2"]
print(items)

##### the elements from position 1 until the end position are replaced
items[1:] = ["Test1", "Test2"]
print(items)

### Sorting Lists
#### TypeError: '<' not supported betwen instances of 'int' and 'str'
#### items = ["Roger", 1, "Syn", True, "Quincy", 7] 
##### lower case later: 'beau'
items = ["Roger", "beau", "Beau", "Quincy"]
items.sort()
print(items)

##### No matter lower case and the sort is in-place
###### If a key function is given, apply it once to each list item and sort them
###### You can copy a list before sorting 
# items_ori = items # TODO: will get the sorted list, why?
items_ori = items[:]
items.sort(key=str.lower, reverse=True)
print(f"Sorted items: {items}")
print(f"Original items: {items_ori}\n")

##### Use global function `sorted` without modifying original list
print(sorted(items, key=str.lower))
print(f"Original items after calling sorted function: {items}")

# Tuples
## In mathematics, a tuple (UK: /ˈtuːpəlˌˈtʃuːpəlˌˈtjuːpəl/ TOO-pəl,TSHOO-pəl,TYOO-pel, US: /ˈtuːpəlˌˈtʌpəl/ TOO-pəl, TU-pəl) 
## is a finite ordered list (sequence) of elements.

## Q. Why are tuples noisier than lists?
### A. Tuples are imMUTEable. # the elements in tuple cannot be modified 

## Syntax: ()
names = ("Roger", "Syd")
### can be indexed like "list"
names[0]
names.index("Roger") # 0
names[-1]
len(names)
print("Roger" in names)
print(sorted(names))

### extend the tuple
newTuple = names + ("Tina", "Qnincy") 
print(newTuple)

# Dictionaries
## different to list
### list allow you to create collections of values, 
### dictionaries allow you to create key value pairs

## Syntax: by curly braces { }
### key can be any immutable value: string, tuple, etc.
### the value can be anything you want 
dog = { "name": "Roger", "age": 8 } # or use single qoute 'name'
print(dog)
cat = { newTuple : "Kyle" } # use tuple as key
print(cat)

## access individual key values
print(dog["name"])
print(dog['name'])

### change value stored at a specific index 
dog["name"] = "Syd"
print(dog)

### another way to get a specific element: get()
#### you can add a default value
print(dog.get("color"))
print(dog.get("color", "brown"))
dog = { "name": "Roger", "age": 8, "color": "green" } # or use single qoute 'name'

### Pop out a specific element: pop()
print(dog.pop("name")) # the "name" is pop
print(dog) # "name" is not printed

### Pop out the last itme: popitem()
print(dog.popitem()) # the "color" is pop
print(dog) # "color" is not printed

## check whether the key is contained in a dictionary: by `in` operator
print("color" in dog) # False
print("age" in dog)   # True

## Add a new key value pair to the dictionary
dog["favorite food"] =  "Meat"
print(dog)

## Get a list with the keys in the dictionary
print(dog.keys())
### To return just the list part instead of `dict_keys` 
cat = []
cat = dog.keys() # TypeError: 'dict_keys' object is not subscriptable
cat = list(dog.keys())
print(cat[0]) # the first element is printed

### can also get a list with the values
print(list(dog.values()))

## return all the items in the list: item()
cat = list(dog.items())
print(cat)
print(cat[1])

## you can also check the number of element of a dictionary
print(len(dog))

## Delete a key value pair
if 'color' in dog:
    del dog['color']
else: 
    print(f"dog is not in the dictionary: {dog}")

## Copy a dictionary
dogCopy = dog.copy()
print(dogCopy)

# Sets
## Sets kind of work like tuples but they're NOT ordered and
## immutable, so you can change them.
##
## You can also say that they kind of work like Dictionary but
## they don't have keys.
##
## They have an immutable version of a set called a "frozen set"
##

### Syntax: { } 

### Sets work well when you think about them as mathematical sets
set1 = {"Roger", "Syd"}
set2 = {"Roger"}

#### intersect
intersect = set1 & set2
print(intersect)

#### a union of two sets
##### mod for modification
set2 = {"Luna"}
mod = set1 | set2
print(mod)

#### check difference by minus '-'
minus = set1 - set2
print(minus)

#### check whether a set is a superset of another 
print(set1 > set2) # False
set2 = {"Roger"}
print(set1 > set2) # True 

### len/list/in can also be used

### ** A set cannot have two of the same item **
set1.add("Roger") 
print(set1) # only one "Roger" will be printed

# Function
## create a set of instructions that we can run when needed
### a function can accept one or more parameters 
#### Parameters: the value accepted by the function and inside the function definition 
def hello():
    print('hello!')

hello() 
hello()
hello()

### also an argument can have a default value that's applied if the argument is not specified
### arguments are the values we pass to the function when we call it
def hello1(name="my friend", age=37):
    print("Hello " + name + " you are " + str(age) + " years old" + '!')

hello1()
hello1("Beau", 18)

## parameters are passed by reference, all types in python are objects
## but some of them are immutable, including `integers`, `booleans`, 
## `floats`, `strings` and `tuples`

### passed by value
def change(value):
    value = 2

val = 1
change(val)
print(val)

### passed by reference 
def pass_by_ref(value):
    #value = 2 # do not change the value in passed list
    value[0] = 2

val = [1] 
pass_by_ref(val)
print(val)

## return a value by return statement
### have the return statement in a conditional so that's a common way to
### end a function if the starting condition is not met
def hello3(name):
    if not name:
        return
    print("Hello " + name + '!')
hello3(False) # nothing to print
hello3("ASa")

### you can also return multiple values
#print(hello4("Syd")) # NameError: name 'hello4' is not defined
def hello4(name):
    return name, "Beau", 8

print(hello4("Syd")) # NameError: name 'hello4' is not defined

## Variable scope
### Variable is visible in parts of your program depending on where you declare it

#### Global variable: if you declare a variable outside a function, 
#### the variable is visible to any code running after the declaration including functions 
age_g = 8
print(age_g)
def test():
    #### Local variable: the variable is declared inside a function
    age_l = 8
    age_g = 16
    print(age_g) # 16 in test()

test()
print(age_g) # the var age_g is used by value in test(), so the value is still 8
# print(age_l) # Error: "age_l" is not defined. Because it's a local variable of test() 

## (*) Nested Functions
### A function defined inside a function is visible only inside that function
### This is useful to create utilites that are useful to a function but not useful outside of it
#### Kyle: like `protected` method in a class
#### Benefit: we can make use of `closures` which we'll talk more about later
def talk(phase):
    def say(word):
        print(word)

    words = phase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')
print()

### If you want to access a variable defined in the outer of function from the inner function: use `nonlocal`
#### `nonlocal` is especially useful with Closures
def count():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)

    increment()

count()
print()
## Closures 
### closure is a special way of doing a function in python if you RETURN A 
### NESTED FUNCTION that nested function has access to the variable defined in 
### that function even if that function is not (?)active anymore
print("*** Closures ***")
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment # RETURN A NESTED FUNCTION

# Instead of just calling the function directly the outer function,
# assign the other function to a variable as the nested function 
increment = counter() 

# The count will not be reset to zero on each call
# We return the increment inner function and has access to the state of the 
# count variable even though the counter function has ended
print(increment()) # 1
print(increment()) # 2
print(increment()) # 3

# Objects
print("*** Objects ***")
## `age` now has access to the properties and methods defined for all `int` 
## objects, this includes for example access to the real and imaginary part of 
## that number
age = 8
print(age.real)
print(age.imag)

### the number of bits necessary to represent this number in binary notation: 
###bit_length()
print(age.bit_length())

## A variable holding a `list` value has access to ** a different set of methods **
### methods of pin and pop, and the methods available to an object, depend on the type of value
items = [1, 2]
items.append(3)
items.pop()

### The ID global function provided by python lets you inspect the location in memory for a particular object
print(id(items))

## Some objects are MUTABLE while others are IMMUTABLE that depends on the object ifself, if the object provides methods to change its content then it's mutable, otherwise it's immutable
## Most type defined by Python are immutable
### An int is immutable, there are not methods to change its value
### if you increment the value, it's actually going to create an entirely new value, so it's not going to even be the same object at all, you has to create a whole new one to reassign it
age = 8
print(id(age)) # 4311886352
age = age + 1
print(id(age)) # 4311886384

### in a dictionary, it would actually be the same object but you could just change different parts of it
dic = {"Kyle": 1, "Rain": 2}
print(id(dic))
dic["Kyle"] = 3
print(dic)
print(id(dic)) # the same id

# Loops
print("\n*** Loops ***")
## while loops
condition = True
while condition == True:
    print("The condition is True")
    condition = False

count = 0
while count < 10:
    print(f"{count}: The condition is True")
    count += 1

print("After the while loop")

## for loops
print("\n=== Iterate element in a list ===")
items = [1, 2, 3, 4]
for item in items:
    print(item)

print("\n=== if we want the index of the list, using `enumerate` ===")
item = ["beau", "syd", "quincy"] 
for index, item in enumerate(item):
    print(index, item)

print("\n=== Iterate a specific amount of times using the `range` function ===")
for item in range(15):
    print(item)

print("\n*** Loops ***\n")