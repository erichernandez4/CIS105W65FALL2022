f = open("data.txt", "r")


counter = 0
all_bonus = 0

last_name  = str(f.readline())


while last_name != " ":
  salary = float(f.readline())

  if salary >= 100000.00:
    bonus  = 0.20
  elif salary > 100000 or salary> 50000:
    bonus = 0.15
  else:
    bonus = 0.10

  bonus_pay = salary * bonus 
  all_bonus = all_bonus + bonus_pay 
  counter = counter + 1 

  print("employee last name: ", last_name)
  print("salary:", salary)
  print("Bonus this year:", bonus_pay)
  print(" ")

  last_name  = f.readline()

print("All the bonuses", all_bonus)

  


