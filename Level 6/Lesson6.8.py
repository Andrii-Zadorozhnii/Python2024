full_name = "James Bond"
first_name = full_name[0:5] #This means we take the first 5 characters
last_name = full_name[6:10] #This means just the last 4 characters
print(f"The first name is {first_name}, and last name is {last_name}")

"""
Exersice

Create a variable (an object) called Titanic.

Then create 3 lines of code tht use 3 ways to print the letter c from Titanic using slicing. 
THREE slicing methodologies (one for each line of code)

"""

an_object = "Titanic"

first_way = an_object[-1]
second_way = an_object[len(an_object)-1]
third_way = an_object[6]

print(first_way)
print(second_way)
print(third_way)