name = 'chris'
print(name.upper())
print(name)

# name = name.upper()
# print(name)

name = "51"
print(name.isdigit())   #True

name = "chris"
print(name.isdigit())   #False

name = " "
print(name.isspace())   #True

name = "chris haroun"
print(name.isspace())   #False

"""
Exersice:

1: Define a variable as jack_name and Assign it to the value Jack
2: Define another variable called empty_glass_case and assign it to one " "
3: Use the method isalpha with jack_name and get python to tell us is the result is true or false
4: Use the method is space with empty_glass_case and get Python to tell us if this is true or false

"""

jack_name = "Jack"
empty_glass_case = " "

x = jack_name.isalpha() 
y = empty_glass_case.isspace()

print(x,y)
