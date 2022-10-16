part_num = float(input("Please enter the part number"))

qty  = float(input("Please enter the quantity"))

if part_num == 10 or part_num == 55:
  unit_cost = 1
elif part_num == 99:
  unit_cost = 2
elif part_num == 80 or part_num == 70:
  unit_cost = 3
else:
  unit_cost = 5

total_cost = qty * unit_cost

print("part number", part_num)
print("Cost per unit ", unit_cost)
print("total cost ",total_cost)


  
  