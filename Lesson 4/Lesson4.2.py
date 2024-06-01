# Asoka is 1.70 meters, Yoda = 0.66, R2D2 = 1.09
#
# 1. Create the variable of height for the 3 characters
asoka_height = float(1.70)
yoda_height = float(0.66)
r2d2_height = float(1.09)
# 2. Create a print line of code that prints this:
#     The average height is [put the average height here]
#     The maximum height is [put the maximum height here]
#     The minimum height is [put the minimum height here]
print("The average height is " + str(round((asoka_height + yoda_height + r2d2_height)/3)))
print("The maximum height is " + str(max(asoka_height, yoda_height, r2d2_height)))
print("The minimum height is " + str(min(asoka_height, yoda_height, r2d2_height)))
# 3. This is tricky, but fun, you have to create additional variables for:
#     Average, minimum, and maximum height
average_heigth = (asoka_height + yoda_height + r2d2_height)/3
maximum_height = max(asoka_height, yoda_height, r2d2_height)
minimum_heigth = min(asoka_height, yoda_height, r2d2_height)

print("The average height is " + str(average_heigth) + ", The maximum height is " + str(maximum_height) + ", The minimum height is " + str(minimum_heigth))







