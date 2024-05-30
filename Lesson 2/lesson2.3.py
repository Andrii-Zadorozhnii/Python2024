# How to Change the Content or Data Type of a Variable
print("------------")

name = "Darth Vader"
print(name)

print("------------")

name = str("Mr. Skywalker")
print(name)

print("------------")

age = "100"
print(type(age))

print("------------")

#   Casting
age = int("100")
print(type(age))

print("------------")

print(int(3.0156))     #   3
print(int(4.9658))     #   4
print(int(5.1658))     #   5

#   Training

#C3P0 is 1.75 meters tall & R2D2 is 1.09 meters tall
#   Step 1: Create a variable called height as a string type
#   Step 2: Assign the height a value of 1.09
#   Step 3: Print the height of R2D2
#   Step 4: Change the height data type from string to floating
#   Step 5: Add 0.66 to 1.09
#   Step 6: Print the new height

height = str()
height = "1.09"
print(height)
height = float(height)
height = height + float(0.66)
print("The Height of R2D2 is: " + str(height))




