# Exersize
'''
Team 1 contain Yoda.
Team 2 contain Jack and Rose
Team 3 has dart Vader and Leah

Part 1: Use the if, elif, else logic
Select Team 1, Team 2, Team 3. Then print:
"You picked team 1, which has 1 character, which is Yoda"
"You picked team 2, which has 2 character, Jack and Rose"
"You picked team 3, which has 2 character, Vader and Leah"

Part 2: Use the add logic. Add additional code to the bottom of Part 1 as follow:
"The number of the people on the team you selected is odd"
"The number of the people on the team you selected is even"

'''


team_1 = "Yoda"
team_2 = "Jack and Rose"
team_3 = "Vader and Leah"

question = input("Please select team, Team 1, Team 2 or Team 3: ")

if question == "Team 1":
    print("You picked team 1, which has 1 character, which is Yoda")
elif question == " Team 2":
    print("You picked team 2, which has 2 character, Jack and Rose")
elif question == "Team 3":
    print("You picked team 3, which has 2 character, Vader and Leah")
else:
    print('Please select team, Team 1, Team 2 or Team 3')

if question == "Team 1" or question == "Team 3":
    print("The number of the people on the team you selected is odd")
else:
    print("The number of the people on the team you selected is even")
