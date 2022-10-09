last_name = input("enter your last name ")
dependents = float(input("enter number of dependents "))
gross_income = float(input("enter your gross income "))

adjusted_gross_income = gross_income - (dependents * 12000)
if adjusted_gross_income >= 50000:
  tax =  0.20
else:
  tax =  0.10

income_tax = adjusted_gross_income * tax
if income_tax < 0:
  income_tax = 100

  
print("Last name ", last_name)
print("This is your gross income ", gross_income)
print("Number of dependents ", dependents)
print("Adjusted gross income ", adjusted_gross_income)
print("income tax ", income_tax)