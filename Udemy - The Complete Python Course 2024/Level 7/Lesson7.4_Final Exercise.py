"""
Level 7 Final Exersice: Restaurant Menu Manager

Objective

You're freelance developer, and a local restaurant has hired you to build a simple menu manager got their Point of Sale system.
They need to frequently update the menu and see how many of each dish they offer.

Instruction:
1. Create a dictionary called menu with keys as dish names and value as tuples containing the dish type and price.
For example, {'Burger': ('Main', 10.5), 'Soup': ('Appetizer',  5.0)}.
    * Dishes it needs to contain: Burger, Soup, Ice Cream, Salad
2.  Add more dishes to the menu - Stake and Soda
3.  Remove a dish from the menu
4.  Create a function called display_menu that takes the menu dictionary and prints out the dishes and their information.
5. Create a function called count_dish_types that takes the menu dictionary and returns a dictionary with dish type as keys and the number of each type of values.
6.  Create a function called update_price that takes the menu dictionary, a dish name, and a new price. It update the price of the dish.
7.  Use all the function you've created to manager the menu and display the updated details.
"""


#   1
menu = {
    'Burger': ('Main', 10.5),
    'Soup': ('Appetizer',  5.0),
    'Ice Cream':('Desert', 0.8),
    'Salad': ('Appetizer', 2.6)
    }

#   2
menu['Stake'] = ('Main', 20.0)
menu['Soda'] = ('Drink', 2.0)
print(menu)

#   3
ask = True
while ask:
    finish = input("Do you want to remove some dish? Y/N ")
    if finish == "Y":
        dish = input("Which dish do you want to remove? ")
        # price = input("What price do you want to set?")
        menu.pop(str(dish))
    else:
        ask = False
        print(" Yours menu: ")
        print(menu)

#   4
def display_menu(menu):
    print("Menu: ")
    for dish, info in menu.items():
        print("Dish:", dish, " | Category: ", info[0], " | Price: ", str(info[1]) + "$")

display_menu(menu)

#   5
def count_dish_types(menu):
    dish_per_category = {}

    for dish, info in menu.items():
        if info[0] in dish_per_category:
            dish_per_category[info[0]] += 1
        else:
            dish_per_category[info[0]] = 1

    return dish_per_category

print(count_dish_types(menu))

#   6
def pdate_price(menu, dish_name, new_price):
    if dish_name in menu:
        menu[dish_name][1] = new_price
    else:
        print("This dish does not exist")