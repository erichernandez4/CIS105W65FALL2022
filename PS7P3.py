def compmpg(miles,gallons):
    mpg = miles/gallons

    return mpg

def compcost(gallons):
    cost_of_trip = gallons * 2.50

    return cost_of_trip

city = input("please enter your city")

miles = float(input("please enter miles travelled"))

gallons = float(input("Enter gallons used "))

mpg = compmpg(miles,gallons)

cost_of_trip = compcost(gallons)

print(city)
print("Miles per gallon ", mpg)
print("cost of gas used in the trip",cost_of_trip)