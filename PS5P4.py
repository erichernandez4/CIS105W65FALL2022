counter = 0 
totalg = 0.00

response = input("Do you want to start this program (yes or no) ")

while response == "yes":
    counter  = counter + 1
    last_name = input("Please enter your last name")
    hours  = float(input("How many hours do you work"))
    payrate = float(input("enter your pay rate"))
if hours > 40:
    gross_pay = (40 * payrate) + (hours - 40 ) * (1.5 * payrate)
else:
    gross_pay = hours  * payrate

print( last_name, "gross pay", gross_pay)
totalg = totalg +gross_pay
response = input("Do you want to start this program (yes or no")


avg_pay = totalg/counter
print("number of employees", counter)
print("average pay is ", avg_pay)





