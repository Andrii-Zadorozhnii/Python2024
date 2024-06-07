"Dictionary {key:value}"

list1 = [1, 2, 3, 4]

print(list1[1:3])

basic_dict = {0: 1, 1:2, 2:3, 3:4}
#every element inside dictionary will have a key and value

print(basic_dict[0])
print(basic_dict[2])

user = {'name': 'Mark', "email": "luka@gmail.com", "number": 12456789}

print(user['name'])

user = {
    'name': 'Mark',
    "email": "luka@gmail.com",
    "number": 12456789,
    "address": {
        "st_name": "Some street",
        "city": "SF",
        "state": "CA"}
    }

print(user['address'])

user['job_title'] = "HR Consultant"

print(user)

print(user.get("name"))
print(user.items())
print(user.keys())
print(user["address"].keys())

number = user.pop("number")

print(user)
print(number)

for val in user.items():
    print(val)

"""
Exersice

Define a dictionary called allegiances with these 3 keys:
1. Luke Skywalker, which has a value of Galactic Empire.
2. Dart Vader, which has a value of Galactic Empire.
3. Obi-Wan Kenobi, which has a value of Jedi Order.

Then print the value of Dart Vader.
Then change the value of Dart Vader from Galactic Empire to Sith Order
Then add another key as followings:
    Leia, which has a value of Rebel Alliance.
    Then print everithing.
"""

allegiances = {
    "Luke Skywalker": "Galactic Empire",
    "Dart Vader": "Galactic Empire",
    "Obi-Wan Kenobi": "Jedi Order"
    }

print(allegiances.get("Dart Vader"))
# Galactic Empire

allegiances["Dart Vader"] = "Sith Order"

print(allegiances)
# {'Luke Skywalker': 'Galactic Empire', 'Dart Vader': 'Sith Order', 'Obi-Wan Kenobi': 'Jedi Order'}

allegiances["Leia"] = "Rebel Alliance"

print(allegiances)
# {'Luke Skywalker': 'Galactic Empire', 'Dart Vader': 'Sith Order', 'Obi-Wan Kenobi': 'Jedi Order', 'Leia': 'Rebel Alliance'}

for keys in allegiances:
    print(f"The keys is {keys}")