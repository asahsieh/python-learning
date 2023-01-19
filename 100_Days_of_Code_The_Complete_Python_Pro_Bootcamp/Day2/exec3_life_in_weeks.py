print(round(8 / 3, 2))
# floor division
print(8 // 3)
result = 4 / 2
result /= 2
print(result)

# F-string: makes it really easy to mix strings and different data types
## using curly braces to place our variables
## like printf() in C
score = 0
height = 1.8
is_winnning = True
print(f"your score is {score}, your height is {height}, you are winning is {is_winnning}")

# Exercise 3 - Life in Weeks
cur_age = input("What is your current age? ")
remain_years = 90 - int(cur_age)
months = remain_years * 12
weeks = remain_years * 52
days = remain_years * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left.")