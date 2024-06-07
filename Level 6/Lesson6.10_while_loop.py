baby_yoda_age = 50

while baby_yoda_age <=100:
    print("You cannot use the lightsaber untill you are 100, You currently " +str(baby_yoda_age))
    baby_yoda_age = int(baby_yoda_age) + 1
    if baby_yoda_age > 90:
        print("I am getting too old")


"""
Exersice

Create a while loop, that prints this:

The year is 1912 and nobody has found the Titanic yet.
The year is 1913 and nobody has found the Titanic yet.
...
Repeat the loop, until 1984.

"""

titanic_sink = 1912

while titanic_sink <= 1984:
    print(f'The year is {titanic_sink} and nobody has found the Titanic yet')
    titanic_sink = int(titanic_sink) + 1