f = open("datatext1.txt", "r")

counter = 0.00
total_tuition  = 0.00

last_name = str(f.readline().rstrip('\n'))

while last_name != "":
  dcode = str(f.readline().rstrip('\n'))
  credits = float(f.readline())

  if dcode == "I":
    cost_per_credit = 250.00
  else:
    cost_per_credit = 500.00


  tuition = cost_per_credit * credits
  counter = counter + 1
  total_tuition = total_tuition + tuition

  print("student: ", last_name)
  print("credits taken", credits)
  print("tuition owed", tuition)
  print(" ")

  last_name =  str(f.readline().rstrip('\n'))

f.close()


print("total number of students", counter)
print("total tuiton owed", total_tuition)