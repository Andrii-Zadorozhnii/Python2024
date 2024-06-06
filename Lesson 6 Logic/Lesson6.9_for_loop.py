"""
Loop
"""

jedis = ["Dart Vader", "Rey", "Yoda", "Leia", "Mr. Skywalker", "Ashoka"]

for name in jedis:
    print( name + " is a jedi.")
    print("-------------------")
    if name == "Yoda":
        break

# for x in "camera":
#     print(x)

for x in range(1,11):
    print(x)

"""
Exersice

Create a for loop, that print 2 lines as follows:

Leia I am your father.
Luka I am your father.

"""

kids = ["Leia", "Luka"]

for i in kids:
    print( i + " I am your father")