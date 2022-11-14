def value_percent(county):
    if county == "cook":
        percent = 0.90
    elif county == "dupage":
        percent = 0.80
    elif county == " mchenry":
        percent  = 0.75
    elif county == "kane":
        percent = 0.60
    else:
        percent = 0.70


response = input("Would you like to start this program ")

while response == "yes":
    county = input("What county are you from")
    value = float(input("Whats the value of your home$"))
    response = input("Would you like to start this program ")
    all_market_values= all_market_values + 0

    
percent = value_percent(county)

assesed_value =  value + (value * percent)

print( " assessed values of the home" , assesed_value)