def sales_report(sales):
    if sales > 100000:
        percent = 0.10
    elif sales <= 100000:
        percent = 0.05
    commission = sales * percent
    nextyears= sales * 1.05
    return commission, nextyears



last_name = input("Please enter your last name")
sales = float(input("Please enter the amount of sales"))
commission, nextyears = sales_report(sales)
print("This is your commission", commission)
print("This is your next years report", nextyears)
