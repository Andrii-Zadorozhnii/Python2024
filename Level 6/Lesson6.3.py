army_size = input("How many characters are in the army? Please only enter 1, 2 or 3 ? ")

if army_size == "1":
    print("The army of 1 will lose to the army of 2 and the army of 3.")
elif army_size == "2":
    print("The army of 2 will beat the army of 1, but lose to the army of 3.")
elif army_size == "3":
    print("The army of 3 beats the army of 2 and the army of 1.")
elif army_size != "1" or "2" or "3":
    print('Please only enter 1, 2 or 3')
else:
    print('Please only enter 1, 2 or 3')
army_size = int(army_size)
print(type(army_size))
print("The cost of the army is " + str(army_size * 10))

if army_size == 1 or army_size ==3:
    print("There are an odd number of characters in the army that you selected")
else:
    print("There are an even number of characters in the army that you selected")

good_or_not_good = input("Type good or not good. ")
if good_or_not_good == "good" and army_size == 1:
    print("You selected an army of 1 and C3P0, which is good")
else:
    print("You did not select an army size of 1 AND good")

