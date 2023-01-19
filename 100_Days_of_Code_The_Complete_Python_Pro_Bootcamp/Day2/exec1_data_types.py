# Data types

# TypeError: object of type 'int' has no len()
# print(len(12345))

# String
# Access a character by 'subscripting',
# the output is: e 
print("Hello"[1])

# Integer

print(123 + 456)

## Split lager number by underscores for more readable 
print(123_456_789)

# Float

3.14159

# Boolean
bool_var = True
True
False
print(bool_var)

# 20. Type Error, Type Checking and Type Conversion
## type()
## int(), str()
## print(str(123), str(456))

# Exercise 1
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")
## Type checking: <class 'str'>
# print(type(two_digit_number))
sum = int(two_digit_number[0]) + int(two_digit_number[1])
print(two_digit_number[0] + " + " + two_digit_number[1] + " = " + str(sum))
print(str(sum))