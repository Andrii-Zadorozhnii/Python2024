# Level 5 Final Exercise: Grocery Shopping List
#
# Objective
#
# You are developing a simple application for managing grocery shopping list.
#
# Instruction:
# 1. Create a list called shopping_list and populate it with the initial items: 'Milk', 'Eggs', 'Bread' and 'Bananas'.

shopping_list = ['Milk', 'Eggs', 'Bread', 'Bananas']

# 2. Add the item 'Apples' to the end of the list.

shopping_list.append('Apples')

# 3. Remove 'Bread' from the list.

shopping_list.remove('Bread')

# 4. Create a function named show_list that takes a list as an argument and prints each item on a new line.

def show_list(list):
    print('Your shopping list: ')
    for element in list:
        print(element)

# 5. Create a function named total_items that takes a list as an argument and returns the number of items in the list.

def total_items(list):
    return len(shopping_list)

# 6. Call show_list and total_items with your shopping_list and display the results.

show_list(shopping_list)
print("Total items: " + str(total_items(shopping_list)))