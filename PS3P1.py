qty = float(input("please enter a quantity "))

if qty >= 1000:
  unit_price = 3.00
else: 
  unit_price = 5.00

ext_price = qty * unit_price

tax = ext_price *0.07

total = ext_price + tax 


print("quantity ordered", qty)
print("unit price ", unit_price)
print("extended price", ext_price)
print("tax", tax)
print("total", total)


  