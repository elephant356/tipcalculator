print("Welcome to the tip calculator!")
bill = input("How much is your bill? ")
tip = input("What percent tip would you like to give? ")
guests = input("How many guests are in your party? ")

cash = float(bill)
casham = round(cash, 2)
tipandbill = (((float(tip) /100) * casham) + casham)
pcbill = tipandbill / float(guests)

casham = "{:.2f}".format(casham)

finalbill = (round(pcbill, 2))
finalbill = "{:.2f}".format(pcbill)

print(f"Since your bill is ${casham} dollars and you have {guests} in your party, each of you need to pay ${finalbill} dollars. ")
