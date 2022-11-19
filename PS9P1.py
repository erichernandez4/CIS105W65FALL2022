def discount(qty,price,discountr):
    total = qty * price 
    disamount = discountr * total
    disprice = total - disamount
    return disamount, disprice



qty = float(input("Enter the quantity "))
price = float(input("Enter the price"))
discountr = float(input("Enter the discount rate %"))
disamount , disprice = discount(qty,price,discountr)


print("This is your quantity ", qty)
print("This is your price ", price)
print("This is your discounted amount $ ", disamount)
print("This is your discounted price total $", disprice)