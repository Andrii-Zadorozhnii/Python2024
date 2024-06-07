ticket = input("What class of ticket do you want to buy for the Titanic? Select 1, 2 or 3\n")

print(f"You selected class number {ticket}")

if ticket == "1":
    price = 870
    print(f"price for current clas is {price:.2f} pounds")
else:
    price = 7
    print(f"price for current clas is {price:.2f} pounds")

# print(type(price))