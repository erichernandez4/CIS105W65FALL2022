number_of_books = float(input("Please enter the number of books "))

cost_per_book = float(input("Please enter the cost per book "))

order_total = cost_per_book * number_of_books

if order_total > 50.00:
  shipping = 0
else:
  shipping = 25.00

print("This is the order total", order_total)
print("This is the shipping charge ", shipping)