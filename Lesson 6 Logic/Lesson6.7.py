"""
Exersice

Rose will purchase a 1st class ticket for 870 pounds.
A 2nd class ticket (for baby Yoda) coasts 10.42 pounds.
A 3rd class ticket (for Jack) is 7 pounds.

-Code this: How many 1st, 2nd and 3rd class tickets do you want to purchase?
-Then print this: The Total price is X pounds.
-Please use the formatting feature with 2 decimal points.

"""
first_class_tickets = input('How many 1st class tickets do you want to purchase?\n')
second_class_tickets = input('How many 2nd class tickets do you want to purchase?\n')
third_class_tickets = input('How many 3rd class tickets do you want to purchase?\n')

final_price = (int(first_class_tickets) * 870) + (int(second_class_tickets) * 100.42) + (int(third_class_tickets) * 7)

print(f"The Total price is {final_price:.2f} pounds")
