def comptotal(qty,price):
    total = float(qty) * float(price)

    if total > 10000.00:
        total = total * 0.90
    else:
        total = total
    return total

qty = float(input("please enter quantity "))
price = float(input("please enter price "))

total = comptotal(qty,price)

print("total is $", total)

