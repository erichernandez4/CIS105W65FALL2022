qty = float(input("Enter the number of tickets"))
if qty >= 25:
  price = 5

elif qty > 24 or qty >10:
  price = 60
elif qty > 9 or qty > 5:
  price = 70
else:
  price  = 75

total_cost = qty * price

print("number of tickets ", qty)
print("price per ticket", price)
print("total cost ", total_cost)