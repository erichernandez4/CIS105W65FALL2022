def ticket_price(miles):
    if miles >= 30:
        price = 12
    elif miles>= 29 or miles>= 20:
        price =10
    elif miles >= 19 or miles >= 10:
        price = 8
    else:
        price = 5 
    return miles
counter = 0
all_ticket_prices = 0 
response = input("Do you want to start this program (yes or no) ")

while response == "yes":
    last_name = input("Please enter your last name ")
    miles = float(input("How many miles are you away from downtown chicago "))
    response = input("Do you want to start this program (yes or no) ")
    counter = counter 

price = ticket_price(miles)
all_ticket_prices = all_ticket_prices + price

print("This is your ticket price", price)
print("All price ticekts", all_ticket_prices)
