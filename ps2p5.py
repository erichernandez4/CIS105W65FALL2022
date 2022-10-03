price = float(input("Please enter price of item $"))
discount_percent = float(input("Please enter the discount percent "))

discount_amount = price * (discount_percent * 0.01)
discount_price = (price -discount_amount )

print("This is the discount amount $",discount_amount )
print("This is the discount price total $",discount_price)