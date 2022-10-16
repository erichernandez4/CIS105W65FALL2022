qty = float(input("Please input the quantity"))

if qty > 10000:
  price = 10

elif qty > 5000:
  price = 20
else:
  price = 30

ext_price = qty * price
tax = ext_price *0.07
total = tax + ext_price

print("extended price ", ext_price)
print("tax amount ", tax)
print("total ", total)