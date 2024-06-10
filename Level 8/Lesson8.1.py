# Methods

name = str('Rey')

print(dir(name)) # all medhods

print(name.upper()) #all uppercase

print(name.lower()) #all lowercase

# count all arguments and need something for count
print(name.count("y"))

print(name.replace("y", "d"))

"""
Exercise
1. Create a variable called name2 and assign to it this: C3P0
2. On one line of code use the print function and the replace method to change the name from C3P0 to R2D2

"""

name2 = "C3P0"
print(name2.replace("C3P0", "R2D2"))