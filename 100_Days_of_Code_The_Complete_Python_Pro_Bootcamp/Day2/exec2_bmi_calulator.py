print(6 / 3)
2 ** 3

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
height = input("enter your height: ")
weight = input("enter your weight: ")
height_as_float = float(height)
weight_as_float = float(weight)
# print(type(height))
bmi = weight / (height ** 2)
print(int(bmi))