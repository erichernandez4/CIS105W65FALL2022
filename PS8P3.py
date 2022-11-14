def percent_off_msrp(model,make,ev_car):
    if make and model == "honda" and "accord":
        percent  = 0.10
    elif make  and model == "toyota " and "rav4":
        percent = 0.15
    elif ev_car == "yes":
        percent = 0.30
    else:
        percent = 0.05
        return percent

total_new_msrp = 0 
total_msrp = 0

response = input("do you want to start this program")

while response == "yes":
    make = input("what is the make of the car ")
    model = input("what is the model of the car ")
    ev_car = input("Is this a electric vehicle(yes or no) ")
    msrp = float(input("What is the MSRP of the car $"))
    response = input("do you want to start this program")
    total_msrp  = total_msrp + msrp

discount = percent_off_msrp(model,make,ev_car)


tax = msrp * 0.07
new_msrp = msrp - (msrp * discount) + float(tax)  


total_new_msrp = total_new_msrp + new_msrp

print("This is the new total of your car ",new_msrp)
print("total of all msrp", total_msrp)
print("total of all sales of cars", total_new_msrp)



