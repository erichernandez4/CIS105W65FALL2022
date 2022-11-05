def comptuition(credit,code):
    if code == "i":
        cost = 250
    else:
        cost = 550
    tuition_total = cost * credit

    return tuition_total

last_name = input("Please enter your last name ")
credit = float(input("please enter your credits taking this semester "))

code = input("please enter district code (i or o) ")

tuitiontotal = comptuition(credit,code)

print(last_name)
print("This is the tuition you owe ", tuitiontotal)