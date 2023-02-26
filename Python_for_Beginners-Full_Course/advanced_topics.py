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

### map() : run a functio upon each item in a iterable item like a list and 
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