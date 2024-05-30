#You've just been hired as a junior developer at a travel agency? and your first task is to create a simple currency converter.
#Your program will convert US Dollars(USD) to Euros (EUR)

# Instruction
print('------------')
# 1. Create a variable named usd_amount and assign it the value of 100
usd_amount = 100
print("You have: " + str(usd_amount) + "USD")
print('------------')
# 2. Create a variable named exchange_rate and assign it the value of 0.85 ( this means as equal to 0.85 EUR)
exchange_rate = 0.85
print("Exchange rate 1 USD = " + str(exchange_rate) + " Euro")
print('------------')
# 3. Perform the conversion by creating a new variable eur_amount. Multiply usd_amount by exchange_rate.
eur_amount = float(usd_amount) * float(exchange_rate)
print("Exchange in progress...")
print('------------')
# 4. Change the data type of eur_amount to an integer.
eur_amount = int(eur_amount)
print('------------')
# 5. Print eur+amount
print("You have after exchange: " + str(eur_amount)+" Euro")
print('------------')