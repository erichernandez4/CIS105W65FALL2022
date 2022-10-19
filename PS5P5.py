counter  = 0 
totaldis = 0.00

response = input("Do you want to start this program")

while response == "yes":
    counter = counter + 1
    qty = float(input("please enter the quantity"))
    price = float(input("please enter the price of item "))
    ext_price  = qty * price 
    if ext_price > 10000:
        discount  = ext_price * 0.25
    else:
        discount = ext_price * 0.10
    total = ext_price - discount 

    totaldis = totaldis + discount
    print("extended price ", ext_price)
    print("discount amount ", discount)
    print("total ", total)
    response = input("Do you want to start this program")


totaldis  = totaldis + 0
print("All of the discounts", totaldis)
