# Level 4 Final Exercise: Simple Calculator with Functions
#
# Objective
#
# You're working on a software team that's building a user-friendly calculator app.
# Your task is build a section of the calculator that performs basic operations (addition, subtraction, multiplication, division) using
# if functions:
#
# Instructions
#
# 1.  Create a function named add that takes two arguments and return their sum.
def add(num1,num2):
    return(float(num1) + float(num2))
# 2.  Create a function named subtract that takes two arguments and returns the results of the first argument minus the second argument.
def subtract(num1,num2):
    return (float(num1) - float(num2))
# 3.  Create a function named multiply that takes two arguments and returns their product.

def multiply(num1,num2):
    return (float(num1) * float(num2))

# 4.  Create function named divide that takes two arguments and returns the result of the first argument divided by the second argument. Round the result to 2 decimal places.

def divide(num1,num2):
    return (float(num1) / float(num2))

# 5. Use the input() function to take two numbers from the user. Make sure to convert them to FLOAT!

num1 = float(input("Please write number 1: "))
num2 = float(input("Please write number 2: "))

# 6. Also use the imput() function to take an operator (either+,-,*, or /).

operator = str(input("Please write operator( +, -, *, /): "))

# 7. Based on the operator, call the corresponding function and print the result. [Done for you :)]

if operator == '+':
    print("The result is: ", add(num1,num2))
elif operator =='-':
    print("The result is: ", subtract(num1, num2))
elif operator =='*':
    print("The result is: ", multiply(num1, num2))
elif operator =='/':
    print("The result is: ", divide(num1, num2))
else:
    print('Invalid operator')




