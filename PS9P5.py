total = 0.00
tax = 0.00



def product(qty,unit_price):
   global total 
   total = qty * unit_price
   global tax 
   tax = total * 0.07 
   return


qty = float(input("Please enter the quantity amount "))
unit_price = float(input("Please enter the price of the item "))

product(qty,unit_price)
print("your total is $ ", total)
print("Tax cost is $ " , tax)