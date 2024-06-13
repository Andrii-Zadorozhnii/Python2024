# 12 more strings methods

name = "Dart Vader"
x = name.split(" ")
print(x)

name = "adasdasd/asdasdsad/dasddasdas/asdasdsa/sadas"
x = name.split("/",1)
print(x)

name = "dasdfsdfsdfsdfs/sdfdsfsd/sdfsdsdf"
x = name.splitlines()
print(x)

name = ("Cristopher","Haroun")
print(type(name))
x = "Andrew".join(name)
print(x)

name = "Chrisy"
x = name.strip("y")
print(x)

name = "      Chrisy       "
print(name)
x = name.strip("")
print(x)

name = "Chrisy    "
x = name.rstrip()
print(x + " end")

name = "    Chrisy"
x = name.lstrip()
print("start " + x)

name = "Dart Vader"
x = int(name.find("D"))+1
print(x)

name = "Dart Vader"
x = name.find("Vader")
print(x)

name = "Dart Vader"
x = name.find("r", 6, 11)
print(x)

name = "Dart Vader"
x = name.index('r')
print(x)

name = "Luke Skywalker"
x = name.replace("Luke", "Anakin")
print(x)

name = "Luke Skywalker"
x = name.count("e", 0, 4)
print(x)

name = "Luke Skywalker"
x = name.startswith('Luke'
)
print(x)

name = "Luke Skywalker"
x = name.endswith('ker')
print(x)

"""
Exersice:

1: Create a variable called name1, and assign it a value of Princess Leia.
Use the split method to split Princess and Leia into 2 words and then print the results.
The answer should look like this: ['Princess','Leia']
2: Create a variable called name2 and assign it the value of Baby Yoda.
Then use lstrip method to remove the word Baby from his name. Then print the results.
3:  Create a variable called name3 and assign it the value of Babay Yoda.
Then use the replace method to replace the word Baby with Master. Then Print the results.

"""
#1
name1 = "Princess Leia"
print(name1.split())
#2
name2 = "Baby Yoda"
print(name2.lstrip("Baby "))
#3
name3 = "Babay Yoda"
print(name3.replace("Babay", "Master"))
