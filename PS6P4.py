f = open("data.txt", "r")

counter = 0 

all_ext_price = 0.00

item = f.readline()

while item != "":
  qty = float(f.readline())
  price = float(f.readline())

  ext_price  = qty * price
  counter = counter + 1 
  all_ext_price = all_ext_price + ext_price

  print("item ", item)
  print("quantity", qty)
  print("extended price",ext_price)
  print(" ")

  item = f.readline()

f.close()

average = all_ext_price / counter

print("all extended prices", all_ext_price)
print("total number of orders", counter)
print("average orders", average)

  
