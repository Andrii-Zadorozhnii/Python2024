# +++++Exersise+++++
#
# 1. Create a function called my_age with 1 variable in brackets called age.
# 2. In the custom function, print my age is [your age].
# 3. Call the function, using the age of 39.
# 4. Change the default age in the function to 19.
# 5. Call the function with nothing in brackets.
age = input('What is you age? ')

def my_age(age):
    print('My age is ' + str(age))

def my_age2():
    age = 19
    print('My age is ' + str(age))

my_age(age)
my_age2()