list1 = [1, 2, 3, 4]

print(list1[3])

list1[3] = 10

print(list1)

tuple1 = (1, 2, 3, 4)

print(tuple1[3])

print(tuple1)

user = ('Luka', 'luka@gmail.com', '321245856', 1, 4.3)

print(user[0])
print(user[1])

print(user.count("Luka"))
print(user.count("Mark"))

for element in user:
    print(element)



"""
Exersice

Add Dart Vader to the Tuple.

Tip: Use casting(which means change a variable type).
    Change the Tuple type to List type
"""

starting_tuple = ("Yoda", "Han Solo", "R2D2", "C3P0")
final_tuple = []

forgotten_character = "Dart Vader"
#___1___
for index in starting_tuple:
    final_tuple.append(index)

print(final_tuple)

final_tuple.append(forgotten_character)

print(final_tuple)

#___2___

starting_tuple = list(starting_tuple)
starting_tuple.append(forgotten_character)
starting_tuple = tuple(starting_tuple)
print(starting_tuple)
