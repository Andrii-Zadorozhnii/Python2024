name = input("What is his name? ")
age = input("What is " + name + "'s age? ")

def age_in_one_year(name,age):
    age_next_year = int(age) + 1
    print("In one year, " + name + " will be " + str(age_next_year) + " years old.")

age_in_one_year(name, age)

# +++++Exersise+++++
#
# 1. Ask who was on the Titanic?
# 2. Ask what year is it currently?
# 3. Print: Jack and Rose were on the Titanic, which sunk 112* years ago.

pessengers = input("Who was on Titanic? ")
year = int(input("What year is it? "))

def pessenger_on_titanic(pessenger_names, year):
    print(pessenger_names + " were on the Titanic, which sunk " + str(year - 1912) + " years ago.")

pessenger_on_titanic(pessengers, year)

# C:\Python312\python.exe "F:/Уроки/Python2024/Level 4/Lesson4.6.py"
#
# What is his name? Andrew
# What is Andrew's age? 32
# In one year, Andrew will be 33 years old.
# Who was on Titanic? Jack and Rose
# What year is it? 2024
# Jack and Rose were on the Titanic, which sunk 112 years ago.
#
# Process finished with exit code 0