item = input("Please enter name of item")

qty = float(input("Please enter the quantity"))

if  item=="A":
  up = 10.00
else: 
  up = 20.00

ext_price = qty * up
print("item ", item)
print("unit price ", up)
print("extended price", ext_price)