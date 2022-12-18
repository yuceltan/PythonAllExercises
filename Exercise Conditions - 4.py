import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print("number1's absolute value greater than number2's absolute value")
elif abs(number1) < abs(number2):
    print("number2's absolute value greater than number1's absolute value")
else:
    print("number2's absolute value equal to number1's absolute value")
