#   You are and intern at aa bank and you have been tasked to create a simple program to calculate the interest that customers will earn on their saving account.
#   Formula: Simple Interest = ( Principal * Rate * Time)/100

#   Instruction
#   1. Create a variable named principal and assign it the value of 1000 (This is the initial amount in USD).
principal = int(1000)
#   2. Create a variable named rate and assign it the value of 5 (Annual interest rate in percentage).
rate = int(5)
#   3. Create a variable named time and assign it the value of 2 (Tim in years).
time = int(2)
#   4. Calculate the simple interest using the formula above. Store the result in a variable named interest.
simple_interest = (principal * rate * time) / 100
#   5. Print the interest amount rounded to 2 decimalplaces along with a message. The message should include the principal, rate, time and interest variables.
print("With a principal amount of " + str(principal) + " USD, at an annual interest rate of " + str(rate) + "%, in "+ str(time) + " years you will earn " + str(simple_interest) + " USD in interest")