last_name = input("Please enter your last name ")
appliance_cost = float(input("Please enter the cost of the appliance "))
if appliance_cost > 1000:
  warranty = appliance_cost * 0.10
else:
  warranty = appliance_cost * 0.05

total = warranty + appliance_cost

print("Last name ", last_name)
print("Cost Of Appliance ", appliance_cost)
print("cost of warranty ", warranty)
print("This is the total ", total)