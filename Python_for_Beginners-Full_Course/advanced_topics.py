# Accepting Arguments from Command Line
## use the `sys` module from the std lib
import sys

### $ python3 advanced_topics.py beau 39
### ['advanced_topics.py', 'beau', '39']
print(sys.argv)

### Assign argument to a variable and use the variable
#name = sys.argv[1]
#print("Hello " + name)

## You really would have to do a lot of work using this method
## because you really should validate the arguments 
## make sure the type is correct and you need to print feedback to the user
## if they're not using the program correctly

### Example code
### parser = argparse.ArgumentParser(
###     description='sum the integers at the command line')
### parser.add_argument(
###     'integers', metavar='int', nargs='+', type=int,
###     help='an integer to be summed')
### parser.add_argument(
###     '--log', default=sys.stdout, type=argparse.FileType('w'),
###     help='the file where the sum should be written')
### args = parser.parse_args()
### args.log.write('%s' % sum(args.integers))
### args.log.close()

import argparse

parser = argparse.ArgumentParser(
    description='This program prints the name of my dogs'
)

# Commands: 
# - $ python advanced_topics.py -c red
# - $ python advanced_topics.py -c # will return help and get an error 
# The parameter `choices` is to bound the valid choices
#parser.add_argument('-c', '--color', metavar='color', required=True, choices={'red', 'yellow'}, help='the color to search for')
parser.add_argument('-c', '--color', metavar='color', required=False, choices={'red', 'yellow'}, help='the color to search for')

args = parser.parse_args()

print(args.color)

# Lambda Functions
## also called anonymous functions, are tiny functions they have no name and only have one expression as their body, and it has not a statement
### An expression returns a value, a statment does not 

### In the "Lambda calculus": https://en.wikipedia.org/wiki/Lambda_calculus
#### Lambda calculus is Turing complete, that is, it is a universal model of computation that can be used to simulate any Turing machine.[2] Its namesake, the Greek letter lambda (λ), is used in lambda expressions and lambda terms to denote binding a variable in a function.
lambda num : num * 2

## can accept multiple arguments
## can not be invoked directly but you can assign them to variables
multiply = lambda a, b : a * b

print(multiply(2, 4))

## The utility of lambda functions comes when combined with other python functionality: in combination with map filter and reduce
print("*** Global functions: map(), filter(), reduce() ***")

### map() : run a functio upon each item in a iterable item like a list 
print("=== map() ===")

### create a new list with the same number of items but the values of each item can be changed
numbers = [1, 2, 3]

def double(a):
    return a * 2
# map(func, *iterables)
result = map(double, numbers)

print(list(result))

#### when the function is a one-liner, it's common to use a lambda function 
double_lamb = lambda a : a * 2
result = map(double_lamb, numbers)
print(list(result))

##### the lambda function can be put right in the same line within the map
result = map(lambda a : a * 2, numbers)

##### the original list is left untouched in a new list with the updated values is returned by map. The result is a map object which is an iterable, so that's why we needed to cast it to list to print its content.
print(list(result))

### filter() takes an iterable and returns a filter object
### which is another iterable but without some of the original items,
### so you can do so by returning true or false from the filtering function
print("=== filter() ===")

numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda n : n % 2 == 0, numbers) 
print(list(result))

### reduce() is used to calculate a value out of a sequence like a list
print("=== reduce() ===")

#### An example that summarizing expenses in a list of tuples
expenses = [
    ('Dinner', 80), # list of expenses stored as tuples
    ('Car repair', 120)
]

sum = 0
for expense in expenses:
    sum += expense[1] # the second element in a tuple 

print("Total expense is " + str(sum))

#### different to map and filter, it's not available automatically,
#### we have to import it fomr the standard library functools
from functools import reduce

# Arguments `a` is the accumulated value and `b` is the updated value from the iterable
# the numbers at the first index are reduced all into down to one value by adding them all together
## for instance:
### b = expense[0][1] = expense[0][1] + expense[1][1] = 80 + 120 = 200
### a = sum = b on this example 
sum = reduce(lambda a, b: a[1] + b[1], expenses)

print("Total expense from reduce() is " + str(sum))
print("***************************************************")

# Recursion: a function in python can call itself
print("***** Recursion *****")

## a common way to explain recurision is by using the factorial calculation
## 3! = 3 * 2 * 1 = 6
def factoria(n):
    if n == 1: return 1
    return n * factoria(n-1)

print(factoria(3))
print("*********************\n")

# Decorators: change the behavior of a function without modifying the function itself
## like the usage of callback function
print("***** Decorators *****")

## An good examples are when you want to add logging test performance perform caching, verify permissions and so on.
## You can also use one when you need to run the same code on multiple functions  

def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("hello")

hello()

print("**********************\n")

# Another way to write comment for code
#
# You can use the help global function to get the documentation for a class, a method, a function or a module.
# And standards allow us to have tools to extract doc strings and automatically generate documentation for your code.
print("***** docstrings *****")

## for a function
def increment(n): 
    """Increment a number"""
    return n + 1

print(help(increment))

## for a class
### It's also common to add docs place a doc string at the top of the file 
### by multiple line docstring
"""Dog module

This module does ... bla bla bla and provides the following classes:

- Dog
...
"""
class Dog:
    ### constructor
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print("WOF!")

print(help(Dog))
print("**********************\n")

# Annotations
## Python is dynamically typed, so we do not have to specify the type of a variable or function parameter or a function return value
## Annotations allow us to optionally do that, so if we want to actually show what type we're expecting for different values.
## Python will actually ignore annotations, a separate tool called `mypi` can be run standalone or integrated by IDEs to automatically check for type errors statically while you're coding

### We make this function only accept an int
def increment_int(n: int) -> int:
    return n + 1

### Add an annotation to make the `count` variable be an int
count: int = 0

# Exceptions
## For exception handling you would wrap lines of code in a `try` block and then
## inside the block you'll put the lines of code.
## And then if an error occurs, python will alert you and you can determine which kind of error occurred using an accept block 
print("***** Exceptions *****")

## template
# try:
#     # some lines of code
# except <ERROR1>:
#     # handler <ERROR1>
# except <ERROR2>:
#     # handler <ERROR2>
# except:
#     # catch all exceptions using an except without an error type
# else: 
#     # no exceptions were raised, the code ran successfully 
# finally:
#     # always run at the end whether or not there are exceptions or no exceptions

### Example: get the error of "ZeroDivisionError: division by zero"
# result = 2 / 0
# print(result)

# Use `finally` to recover gracefaully and move on with the program 
try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divid by zero!')
finally:
    result = 1

print("result = " + str(result)) # 1

## You can Raise an Exception intentionally
## the program will be stoped
# raise Exception('An error!')

### or intercept it by the try block and it's not stopping our program 
try: 
    raise Exception('An error!')
except Exception as error:
    print(error)

## You can also define your own exception class extending from exception
class DogNotFoundExpception(Exception):
    # `pass` here just means nothing and we must use it when we define a class without methods or a function without code
    print("inside")
    pass

try:
    raise DogNotFoundExpception()
except DogNotFoundExpception:
    print('Dog not found!')

### `with` statement
### is very helpful to simplify working with exception handling

#### for example when working with files, each time we open a file we must remember to close it. `with` makes the process more transparent 

##### An example to open/close file without the `with` statement 
filename = './test.txt'

try:
    # file = open(filename, 'r')
    # content = file.read()
    # print(content)

    ## An alternate way by `with`
    ## It's going to make sure to automatically close the file at the end
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as error:
    print("File not found!")
finally:
    file.close()
print("**********************")

# pip: third-party package
#
# The modules are all collected in a single place called the "python package index" which is available at pypi.org, and they can be installed on the system using `pip`

## Commands: $ pip install <package>
##  upgrade: $ pip install -U <package>
##           $ pip uninstall <package>
##           $ pip show <package>

# List Compressions
#
# A way to create lists in a very concise way

print("***** List Compressions *****")
numbers = [1, 2, 3, 4, 5]

## sometimes preferred over loops as it's more readable when the operation can be written on a single line
numbers_power_2 = [n**2 for n in numbers]

print(f"numbers: {numbers}")
print(f"numbers_power_2: {numbers_power_2}")

## This is how you would do it with a loop
## We take a few lines to do
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)

## You can do the same thing with map as well
numbers_power_2 = list(map(lambda n : n**2, numbers))
print(f"numbers_power_2 by `map`: {numbers_power_2}")
print("*****************************\n")

# Polymorphism generalizes a functionality, so it can work on different types
# On functions
print("***** polymorphism *****")

## Example: `cat` function on different classes
##
### Code in the basic_topics will be executed
## from basic_topics import Animal 
class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal):
    def walk(self):
        print('Dog walks')

class Cat(Animal):
    def walk(self):
        print('Cat walks') 

animal = Dog()
animal.walk()
animal = Cat()
animal.walk()

print("************************\n")

# Operator Overloading
#
# Make classes comparable and to make them work with python operators

print("***** Operator Overloading *****")

## An example that we want to compare age of Dogs by __gt__ function
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # `other` is used to specify other object to compare 
    def __gt__(self, other):
        return True if self.age > other.age else False

roger = Dog('Roger', 8)
syd = Dog('Syn', 9)

print(roger > syd)

### Different arithmetic operators 
#### __add__() respond to the + operator
#### __sub__() respond to the - operator
#### __mul__() respond to the * operator
#### __truediv__() respond to the / operator
#### __flodrdiv__() respond to the // operator
#### __mod__() respond to the % operator
#### __pow__() respond to the ** operator
#### __rshift__() respond to the >> operator
#### __lshift__() respond to the << operator
#### __and__() respond to the & operator
#### __or__() respond to the | operator
#### __xor__() respond to the ^ operator

print("********************************\n")