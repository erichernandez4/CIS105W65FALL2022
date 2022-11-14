def months_forecast(month):
    if month in ("jan" "feb" "march"):
        percent = 0.10
    elif month in ("apr" "may" "jun"):
        percent = 0.15
    elif month in  ("jul" "aug" "sep"):
        percent = 0.20
    else:
        percent = 0.25
    return percent 

response = input("Would you like to start this program")

while  response == "yes":
    last_name = input("please enter your last name ")
    month = input("Month of the year ")
    sales = float(input("How many sales did you have "))
    response = input("Would you like to start this program")



percent  = months_forecast(month)
next_month_sales = sales * ( 1 + percent)




print("This is your percent ", percent)
print("This is your next months sales $" , next_month_sales)

