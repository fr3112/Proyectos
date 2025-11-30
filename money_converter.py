#This program takes an amount of US dollars and convert it to different currencies.

USD_TO_MXN = 18.35
USD_TO_EUR = 0.86
USD_TO_GTQ = 7.64
USD_TO_HNL = 26.26
USD_TO_ASR = 1446.81
USD_TO_PEN = 3.36
USD_TO_CLP = 925.93
USD_TO_COP = 3735.59
USD_TO_JPY = 156.15
USD_TO_CNY = 7.08

try:
    amount = float(input("\n-What is your amount? "))
except ValueError:
    print("Error: write a valid amount.")
    exit()

if amount < 0:
    print("Error: the amount can't be negative.")
    exit()

print("\n-Choose the currency you want to convert your amount to.")
print("\n*Japanese yen")
print("*Mexican peso")
print("*Quetzal")
print("*Argentine peso")
print("*Renminbi")
print("*Chilean peso")
print("*Colombian peso")
print("*Lempira")
print("*Euro")
print("*Peruvian soles")

currency = input("\n-Put the currency you want to convert to here: \n")

if currency == "Japanese yen":
    temp = amount * USD_TO_JPY

elif currency == "Mexican peso":
    temp = amount * USD_TO_MXN

elif currency == "Quetzal":
    temp = amount * USD_TO_GTQ

elif currency == "Argentine peso":
    temp = amount * USD_TO_ASR

elif currency == "Renminbi":
    temp = amount * USD_TO_CNY

elif currency == "Chilean peso":
    temp = amount * USD_TO_CLP

elif currency == "Colombian peso":
    temp = amount * USD_TO_COP

elif currency == "Lempira":
    temp = amount * USD_TO_HNL

elif currency == "Euro":
    temp = amount * USD_TO_EUR

elif currency =="Peruvian soles":
    temp = amount * USD_TO_PEN

else:
    print("Error: invalid option.")
    exit()

result = round(temp, 2)

print(f"\n-The amount in {currency} is {result}.-")