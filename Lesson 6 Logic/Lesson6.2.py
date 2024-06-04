jedi_test = input("Is it character holding lightsaber? ")

if jedi_test == "Yes":
    print("The character is a jedi.")
    color = input("Is the lightsaber red? ")
    if color == "Yes":
        print("The character is Dart Vader.")
else:
    print("The character is not a jedi.")

# Exersice
#
# Create 2 statements, as follows:
#
# 1:  Is the character holding a lightsaber?
# 2:  Is the lightsaber green. If so, then print: The character is Yoda

jedi_question = input("Is the character holding a lightsaber? ")
if jedi_question == "Yes":
    print("The character is jedi.")
    color = input("Is the lightsaber green? ")
    if color == "Green":
        print("The character is Yoda")
else:
    print("The character is not a jedi")
