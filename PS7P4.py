def comppayrate(code):
    if code =="L":
        payrate = 25.00
    elif code == "a":
        payrate = 30.00
    else:
        payrate = 50.00

    return payrate


def compgrosspay(hours,payrate):
    if hours > 40:
        grosspay = (40 * payrate) + (hours - 40) * (1.5 * payrate)
    else:
        grosspay = hours * payrate 

    return grosspay

last_name = input("please enter last name ")
code = input("please enter level code (L,a,j) ")
hours  = float(input("please enter hours worked "))

payrate = comppayrate(code)
grosspay = compgrosspay(hours,payrate)

print(last_name)
print("This is your gross pay ", grosspay)